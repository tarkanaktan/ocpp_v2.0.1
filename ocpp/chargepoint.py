from dataclasses import asdict
from typing import Dict, List, Union
from jsonschema.exceptions import ValidationError as SchemaValidationError
import asyncio
import inspect
import uuid
import logging
import time

from ocpp.messagetypes import Call, MessageType, unpack
from ocpp.validator import validatePayload
from ocpp.routing import create_route_map

import ocpp.ocppmessages.outgoingmessages as outgoingmessages
import ocpp.ocppmessages.incomingmessages as incomingmessages

from ocpp.exceptions import (
    OCPPError,
    NotSupportedError,
)

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

class ChargePoint():

    def __init__(self, id, connection, connectorid, response_timeout=30):

        self.id = id
        self.response_timeout = response_timeout
        self._connection = connection
        self.connectorid = connectorid
        self.online = False

        self._call_lock = asyncio.Lock()

        # A queue used to pass CallResults and CallErrors.
        self._response_queue = asyncio.Queue()

        self.route_map = create_route_map(self)

        # Function used to generate unique ids for CALLs. By default
        # uuid.uuid4() is used, but it can be changed. This is meant primarily
        # for testing purposes to have predictable unique ids.
        self._unique_id_generator = uuid.uuid4

        self._call_result = incomingmessages
        self._call = outgoingmessages
    
    async def start(self):
        while True:
            message = await self._connection.recv()
            print("{}: receive message {}".format(self.id, message))

            await self.route_message(message)

    async def route_message(self, raw_msg):

        try:
            msg = unpack(raw_msg)
        except OCPPError as e:
            LOGGER.exception(
                "Unable to parse message: '%s', it doesn't seem "
                "to be valid OCPP: %s",
                raw_msg,
                e,
            )
            return

        if msg.message_type_id == MessageType.Call:
            try:
                await self._handle_call(msg)
            except OCPPError as error:
                LOGGER.exception("Error while handling request '%s'", msg)
                response = msg.create_call_error(error).to_json()
                await self._send(response)

        elif msg.message_type_id in [MessageType.CallResult, MessageType.CallError]:
            self._response_queue.put_nowait(msg)

    async def _handle_call(self,msg):
        #msg has unique_id, action, payload
        try:
            print(self.route_map[msg.action]["_skip_schema_validation"])
            handlers = self.route_map[msg.action]
            if handlers["_skip_schema_validation"] is True:
                validatePayload(msg)
        except SchemaValidationError as e:
            print(e)
        try:
            handler = handlers["_on_action"]
        except KeyError:
            raise NotSupportedError(
                details={"cause": f"No handler for {msg.action} registered."}
            )
        try:
            response = handler()
            if inspect.isawaitable(response):
                response = await response
        except Exception as e:
            LOGGER.exception("Error while handling request '%s'", msg)
            response = msg.create_call_error(e).to_json()
            await self._send(response)
            return

        payload_to_send = asdict(response)
        payload_to_send = self.remove_nones(payload_to_send)
        message = msg.create_call_result(payload_to_send)
        if handlers["_skip_schema_validation"] is True:
            validatePayload(message)
        await self._send(message.to_json())

        try:
            handler = handlers["_after_action"]
        except KeyError:
            raise NotSupportedError(
                details={"cause": f"No handler for {msg.action} registered."}
            )
        try:
            response = handler()
            if inspect.isawaitable(response):
                response = await response
        except Exception as e:
            LOGGER.exception("Error while handling request '%s'", msg)

    async def call(self,payload):
        msg_payload = asdict(payload)
        msg_payload = self.remove_nones(msg_payload)
        action_name = ""
        if "Request" in payload.__class__.__name__:
            action_name = payload.__class__.__name__[:-14]
        elif "Response" in payload.__class__.__name__:
            action_name = payload.__class__.__name__[:-15]
        call = Call(
            unique_id=str(self._unique_id_generator()),
            action=action_name,
            payload=msg_payload,
        )
        await self._send(call.to_json())
        print("{}: send message {} ".format(self.id, call.to_json()))
        try:
            response = await self._get_response(call.unique_id,self.response_timeout)
        except:
            LOGGER.error("No response")

        response.action = call.action
        try:
            validatePayload(response)
        except Exception as e:
            print(e)
            return
        try:
            handlers = self.route_map[response.action]
        except:
            LOGGER.error("Couldn't get handlers with action")
        try:
            handler = handlers["_on_response_action"]
            ret = handler(response)
        except:
            LOGGER.error("Couldn't get handler onresponse")
        cls = getattr(self._call_result, action_name + "ResponsePayload")
        return cls(**response.payload)
        #return self._get_attiribute_list(action_name,response)

    def _get_attiribute_list(self, action_name, response):
        cls = getattr(self._call_result, action_name + "ResponsePayload")
        attribute =  cls(**response.payload)
        print(response.payload.keys())
        for att in response.payload.keys():
            if(isinstance(att, dict)):
                print(att)
        return attribute

    async def _send(self, message):
        LOGGER.info("%s: send %s", self.id, message)
        await self._connection.send(message)

    async def _get_response(self,unique_id,timeout):
        wait_until = time.time() + timeout
        try:
            # Wait for response of the Call message.
            response = await asyncio.wait_for(self._response_queue.get(), timeout)
        except asyncio.TimeoutError:
            LOGGER.error("Timeout")

        if response.unique_id == unique_id:
            return response

        LOGGER.error("Ignoring response with unknown unique id: %s", response)
        timeout_left = wait_until - time.time()

        if timeout_left < 0:
            raise asyncio.TimeoutError

        return await self._get_response(unique_id, timeout_left)

    def remove_nones(self, data: Union[List, Dict]) -> Union[List, Dict]:
        if isinstance(data, dict):
            return {k: self.remove_nones(v) for k, v in data.items() if v is not None}

        elif isinstance(data, list):
            return [self.remove_nones(v) for v in data if v is not None]

        return data
