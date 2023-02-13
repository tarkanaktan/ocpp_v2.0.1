import asyncio
import websockets
import uuid
from websocket.websocketProtocol import WebSocket
from chargepoint import ChargePoint
from ocppmessages import outgoingmessages

async def main():
    connection = WebSocket(uri="ws://localhost:9000/CP_1", subprotocols=["ocpp2.0.1"], ping_interval=None, ping_timeout=None)
    async with connection.connect() as client:
        chargePoint = ChargePoint("CP_1",client,1)
        request = outgoingmessages.BootNotificationRequestPayload(
            charging_station={"model": "XYZ", "vendor_name": "niso"},
            reason="PowerUp",
        )
        print(request)
        await chargePoint.route_message('''[2,"01b779b2-e608-4904-96b0-10a8ab45f7f5","BootNotification",{"chargingStation":{"model":"Wallbox XYZ","vendorName":"anewone"},"reason":"PowerUp"}]''')
        if client.open:
            print("connection established")
            name = '''[2,"01b779b2-e608-4904-96b0-10a8ab45f7f5","BootNotification",{"chargingStation":{"model":"Wallbox XYZ","vendorName":"anewone"},"reason":"PowerUp"}]'''
            await chargePoint._connection.send(name)
            print(f">>> {name}")

            greeting = await chargePoint._connection.recv()
            connection.on_recv(greeting)
            print(f"<<< {greeting}")
        else:
            print("No connection")
        while True:
            name = '''[2,"503bfca3-f677-4305-ad36-70a21d0470d9","Heartbeat",{}]'''
            await chargePoint._connection.send(name)
            print(f">>> {name}")

            greeting = await chargePoint._connection.recv()
            connection.on_recv(greeting)
            print(f"<<< {greeting}")
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())