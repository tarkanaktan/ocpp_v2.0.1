import asyncio

from ocpp.websocket.websocketProtocol import WebSocket
from application.myChargePoint import MyChargePoint
from application.db.variables import Variables


async def main():
    variables = Variables()
    await variables._init_()
    connection = WebSocket(uri="ws://localhost:8000/CP_1", subprotocols=["ocpp2.0.1"], ping_interval=None, ping_timeout=None)
    async with connection.connect() as client:
        chargePoint = MyChargePoint("CP_1",client,variables)
        chargePoint.setConnectorCount(2)
        chargePoint.createEvseObject()
        await asyncio.gather(
            chargePoint.start(), chargePoint.startProcedure()
        )

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
