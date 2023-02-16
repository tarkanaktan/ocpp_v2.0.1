from dataclasses import asdict
import asyncio
import inspect
import uuid
import logging

from messagetypes import Call, MessageType, unpack
from validator import get_validator
from routing import create_route_map
from jsonschema import _validators as SchemaValidators
from jsonschema.exceptions import ValidationError as SchemaValidationError

from exceptions import (
    FormatViolationError,
    NotImplementedError,
    OCPPError,
    PropertyConstraintViolationError,
    ProtocolError,
    TypeConstraintViolationError,
    UnknownCallErrorCodeError,
    ValidationError,
    NotSupportedError,
)

LOGGER = logging.getLogger("ocpp")

class ChargePoint():

    def __init__(self, id, connection, connectorid, response_timeout=30):

        self.id = id
        self.response_timeout = response_timeout
        self._connection = connection
        self.connectorid = connectorid

        self._call_lock = asyncio.Lock()

        # A queue used to pass CallResults and CallErrors.
        self._response_queue = asyncio.Queue()

        self.route_map = create_route_map(self)

        # Function used to generate unique ids for CALLs. By default
        # uuid.uuid4() is used, but it can be changed. This is meant primarily
        # for testing purposes to have predictable unique ids.
        self._unique_id_generator = uuid.uuid4
    
    async def start(self):
        while True:
            message = await self._connection.recv()
            print("%s: receive message %s", self.id, message)

            await self.route_message(message)

    async def route_message(self, raw_msg):

        try:
            msg = unpack(raw_msg)
            print("msg:    ",msg)
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
        print("handle message",msg,msg.payload,msg.action)
        validator = get_validator(msg.message_type_id,msg.action,"2.0.1")
        try:
            print(self.route_map[msg.action]["_skip_schema_validation"])
            handlers = self.route_map[msg.action]
            if handlers["_skip_schema_validation"] is True:
                validator.validate(msg.payload)
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
            print(response)
            if inspect.isawaitable(response):
                response = await response
        except Exception as e:
            LOGGER.exception("Error while handling request '%s'", msg)
            response = msg.create_call_error(e).to_json()
            await self._send(response)
            return

        payload_to_send = asdict(response)
        print("payload_to_send:   ",payload_to_send)
        message = msg.create_call_result(payload_to_send)
        responseValidator = get_validator(MessageType.CallResult,msg.action,"2.0.1")
        print("message:   ",message)
        if handlers["_skip_schema_validation"] is True:
            responseValidator.validate(message.payload)
        await self._send(message.to_json())

    def call(self):
        pass
    async def _send(self, message):
        LOGGER.info("%s: send %s", self.id, message)
        await self._connection.send(message)
