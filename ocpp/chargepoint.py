import websockets
import asyncio
import time
import uuid
import logging

from messagetypes import Call, MessageType, unpack
from exceptions import OCPPError

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

    async def _send(self, message):
        LOGGER.info("%s: send %s", self.id, message)
        await self._connection.send(message)
