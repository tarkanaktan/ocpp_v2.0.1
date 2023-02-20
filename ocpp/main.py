import asyncio
from websocket.websocketProtocol import WebSocket
from chargepoint import ChargePoint,LOGGER
from ocppmessages import outgoingmessages, incomingmessages, messagedictionaries
from dataclasses import asdict
from routing import on,after
from messagetypes import Call

class MyChargePoint(ChargePoint):
    @on("Heartbeat")
    def heartbeat(self):
        print("heartbeat sent")
        pass
    @on("BootNotification",skip_schema_validation=True)
    def on_boot_notification(self):
        print("bootNotification sent on")
        payload = incomingmessages.BootNotificationResponsePayload(interval=5,currentTime="2023-02-15T14:12:12.312173")
        return payload

    @after("BootNotification")
    def after_boot_notification(self):
        print("bootNotification sent after")

    @on("UpdateFirmware")
    def on_update_firmware(self):
        payload = outgoingmessages.UpdateFirmwareResponsePayload()
        return payload
    @after("UpdateFirmware")
    def on_update_firmware(self):
        self.firmwareProcedure.start()
        firmwareUpdateStart_flag = True

    
    async def send_heartbeat(self, interval):
        request = outgoingmessages.HeartbeatRequestPayload()
        while True:
            await self.call(request)
            #await self.route_message('''[2,"8604bf8b-c12c-4de3-924e-1ea3afd8c66c","BootNotification",{"chargingStation":{"model":"Wallbox XYZ","vendorName":"anewone"},"reason":"PowerUp"}]''')
            await asyncio.sleep(interval)

    async def send_boot_notification(self):
        request = outgoingmessages.BootNotificationRequestPayload(
            chargingStation={"model": "Wallbox XYZ", "vendorName": "anewone"},
            reason="PowerUp",
        )
        response = await self.call(request)

        if response.status == "Accepted":
            LOGGER.info("Connected to central system.")
            await self.send_heartbeat(response.interval)

    

async def main():
    connection = WebSocket(uri="ws://localhost:8000/CP_1", subprotocols=["ocpp2.0.1"], ping_interval=None, ping_timeout=None)
    async with connection.connect() as client:
        chargePoint = MyChargePoint("CP_1",client,1)
        cls = getattr(chargePoint._call, "BootNotificationRequestPayload")
        request = outgoingmessages.BootNotificationRequestPayload(
            chargingStation= messagedictionaries.ChargingStationDict(model="ugur",vendorName="ugurderindondurucu"),
            reason="PowerUp",
        )
        msg_payload = asdict(request)
        payload = cls(**msg_payload)
        if isinstance(payload.chargingStation, dict):
            print("dictttttttttttttttttt")
            print(payload.chargingStation.keys())
            for ele in payload.chargingStation.keys():
                print(ele)
        cls2 = getattr(chargePoint._call, "ChargingStationDict")
        payload2 = cls2(**payload.chargingStation)
        print(payload.chargingStation)
        print(payload2.model,payload2.vendorName)
        await asyncio.gather(
            chargePoint.start(), chargePoint.send_boot_notification()
        )
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
