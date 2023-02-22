import asyncio
import random
from datetime import datetime
from ocpp.chargepoint import ChargePoint, LOGGER
from ocpp.routing import onresponse,on,after
import ocpp.ocppmessages.incomingmessages as incomingmessages
import ocpp.ocppmessages.outgoingmessages as outgoingmessages
import ocpp.ocppmessages.messagedictionaries as messagedictionaries

from application.enumtypes import *

class MyChargePoint(ChargePoint):
    @onresponse("Heartbeat")
    def heartbeat(self, *args, **kwargs):
        print("set time with ",args[0].payload)

    @onresponse("BootNotification")
    def on_response_bootnotification(self,*args, **kwargs):
        print("on response of boot")
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
            global actual_state
            await self.call(request)
            #await self.route_message('''[2,"8604bf8b-c12c-4de3-924e-1ea3afd8c66c","BootNotification",{"chargingStation":{"model":"Wallbox XYZ","vendorName":"anewone"},"reason":"PowerUp"}]''')
            await asyncio.sleep(interval-2)
            random_attr = random.choice(ConnectorStatusEnumType.attrlist)
            actual_state = getattr(ConnectorStatusEnumType,random_attr)
            await asyncio.sleep(2)

    async def send_boot_notification(self):
        request = outgoingmessages.BootNotificationRequestPayload(
            chargingStation=messagedictionaries.ChargingStationDict(model="Wallbox XYZ",vendorName="anewone"),
            reason="PowerUp",
        )
        try:
            response = await self.call(request)
            if response.status == RegistrationStatusEnumType.Accepted:
                LOGGER.info("Connected to central system.")
                self.online = True
                await self.send_heartbeat(response.interval)
            elif response.status == RegistrationStatusEnumType.Pending or response.status == RegistrationStatusEnumType.Rejected:
                LOGGER.info("Pending received trying to reconnect to central system.")
                await asyncio.sleep(response.interval)
                await self.send_boot_notification()
        except Exception as e:
            print(e)
    
    async def startProcedure(self):
        await asyncio.gather(
            self.updateStatus(), self.send_boot_notification()
        )

    async def updateStatus(self):
        global actual_state 
        previous_state = ConnectorStatusEnumType.Uninitialized
        actual_state = ConnectorStatusEnumType.Uninitialized
        while True:
            if(previous_state != actual_state):
                request = outgoingmessages.StatusNotificationRequestPayload(timestamp=datetime.utcnow().isoformat(),connectorStatus=actual_state,evseId=self.id,connectorId=self.connectorid)
                await self.call(request)
                previous_state = actual_state
            await asyncio.sleep(1)