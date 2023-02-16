import asyncio
import json
from websocket.websocketProtocol import WebSocket
from chargepoint import ChargePoint,LOGGER
from ocppmessages import outgoingmessages, incomingmessages
from dataclasses import asdict
from routing import on,after

class MyChargePoint(ChargePoint):
    @on("Heartbeat")
    def heartbeat(self, **kwargs):
        print("heartbeat sent")
        pass
    @on("BootNotification",skip_schema_validation=True)
    def on_boot_notification(self, **kwargs):
        payload = incomingmessages.BootNotificationResponsePayload(interval=5,currentTime="2023-02-15T14:12:12.312173")
        return payload

    @after("BootNotification")
    def after_boot_notification(self, **kwargs):
        print("bootNotification sent")
    

async def main():
    connection = WebSocket(uri="ws://localhost:9000/CP_1", subprotocols=["ocpp2.0.1"], ping_interval=None, ping_timeout=None)
    async with connection.connect() as client:
        chargePoint = MyChargePoint("CP_1",client,1)
        request = outgoingmessages.BootNotificationRequestPayload(
            charging_station={"model": "XYZ", "vendor_name": "niso"}
        )
        await chargePoint.route_message('''[2,"01b779b2-e608-4904-96b0-10a8ab45f7f5","BootNotification",{"chargingStation":{"model":"Wallbox XYZ","vendorName":"anewone"},"reason":"PowerUp", "customData":{"vendorId":"aaa"}}]''')
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