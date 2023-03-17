import asyncio
import random
import json
from datetime import datetime
from ocpp.chargepoint import ChargePoint, LOGGER
from ocpp.routing import onresponse,on,after
import ocpp.ocppmessages.incomingmessages as incomingmessages
import ocpp.ocppmessages.outgoingmessages as outgoingmessages
import ocpp.ocppmessages.messagedictionary as messagedictionary

from application.enumtypes import *

transactionOngoing = True
waitTransactionToEnd = False

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

    @on("Reset")
    def on_reset(self,*args):
        global transactionOngoing
        msg_payload = args[0].payload
        print("reset payload", msg_payload, msg_payload["type"])
        try:
            if(msg_payload["evseId"] != 0): 
                payload = outgoingmessages.ResetResponsePayload("Rejected")
        except:
            pass
        try:
            if(msg_payload["type"] == "OnIdle" and transactionOngoing == True):
                payload = outgoingmessages.ResetResponsePayload("Scheduled")
            elif(msg_payload["type"] == "OnIdle" and transactionOngoing == False):
                payload = outgoingmessages.ResetResponsePayload("Accepted")
            elif(msg_payload["type"] == "Immediate"):
                payload = outgoingmessages.ResetResponsePayload("Accepted")
        except:
            pass
        return payload
    @after("Reset")
    async def after_reset(self,*args):
        global waitTransactionToEnd
        reset_response_payload = args[0]
        print("after reset",reset_response_payload,reset_response_payload["status"])
        if(reset_response_payload["status"] == "Accepted"):
            print("reset immediately")
            #TODO
        elif(reset_response_payload["status"] == "Scheduled"):
            print("wait for transcation to end")
            waitTransactionToEnd = True
            #TODO


    @on("ChangeAvailability")
    def on_change_availability(self,*args):
        global transactionOngoing
        global actual_state
        msg_payload = args[0].payload
        print("change availability payload", msg_payload, msg_payload["operationalStatus"],msg_payload["evse"]["id"])
        try:
            if(msg_payload["operationalStatus"] == "Operative" and transactionOngoing == True):
                payload = outgoingmessages.ChangeAvailabilityResponsePayload("Scheduled")
                print("CP is operative and charge is ongoing so changing is scheduled.")
            elif(msg_payload["operationalStatus"] == "Operative" and transactionOngoing == False):
                payload = outgoingmessages.ChangeAvailabilityResponsePayload("Accepted")
                print("CP is operative and there is no charge so changing is accepted.")
                actual_state = "Available"
        except:
            pass
        try:
            if(msg_payload["operationalStatus"] == "Inoperative" and transactionOngoing == True):
                payload = outgoingmessages.ChangeAvailabilityResponsePayload("Scheduled")
                print("CP is inoperative and charge is ongoing so changing is scheduled.")
                actual_state = "Unavailable"
            elif(msg_payload["operationalStatus"] == "Inoperative" and transactionOngoing == False):
                payload = outgoingmessages.ChangeAvailabilityResponsePayload("Rejected")
                print("CP is inoperative and charge is ongoing so changing is rejected.")
                actual_state = "Unavailable"
        except:
            pass
        return payload
    
    @after("ChangeAvailability")
    async def after_change_availability(self,*args):
        global waitTransactionToEnd
        change_availability_payload = args[0]
        print("after change availability",change_availability_payload,change_availability_payload["status"])
        if(change_availability_payload["status"] == "Accepted"):
            print("change immediately")
            #TODO
        elif(change_availability_payload["status"] == "Scheduled"):
            print("wait for transcation to end")
            waitTransactionToEnd = True     



    @on("TriggerMessage")
    def on_trigger_message(self,*args):
        global check
        global msg_payload
        requested_messages=["BootNotification","LogStatusNotification","FirmwareStatusNotification","Heartbeat","MeterValues","SignChargingStationCertificate","SignV2GCertificate","StatusNotification","TransactionEvent","SignCombinedCertificate","PublishFirmwareStatusNotification"] #List of proper messages
        msg_payload = args[0].payload
        print("trigger message payload", msg_payload, msg_payload["requestedMessage"]) 
        try:
            if any(s==msg_payload["requestedMessage"] for s in requested_messages): #Check if coming message matches with one of the proper messages.
                payload = outgoingmessages.TriggerMessageResponsePayload("Accepted")
                print("Triggered message is implemented so I will send it.")
                check=True
                return payload
            else:    
                payload = outgoingmessages.TriggerMessageResponsePayload("NotImplemented")
                print("Triggered message is not implemented so I will not send it.") 
                return payload

        except:
            pass

    
    @after("TriggerMessage")
    async def after_trigger_message(self,*args):
        #trigger_message_payload = args[0]
        try:
            if (check):
                #sending request of triggered message
                
                if msg_payload["requestedMessage"] == "BootNotification":
                    request= outgoingmessages.BootNotificationRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "LogStatusNotification":
                    request= outgoingmessages.LogStatusNotificationRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "FirmwareStatusNotification":
                    request= outgoingmessages.FirmwareStatusNotificationRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "Heartbeat":
                    request= outgoingmessages.HeartbeatRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "MeterValues":
                    request= outgoingmessages.MeterValuesRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "SignChargingStationCertificate":
                    request= outgoingmessages.SignCertificateRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "SignV2GCertificate":
                    request= outgoingmessages.SignCertificateRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "StatusNotification":
                    request= outgoingmessages.StatusNotificationRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "TransactionEvent":
                    request= outgoingmessages.TransactionEventRequestPayload()
                    print(request)
                elif msg_payload["requestedMessage"] == "SignCombinedCertificate":
                    request= outgoingmessages.SignCertificateRequestPayload()
                    print(request)            
                elif msg_payload["requestedMessage"] == "PublishFirmwareStatusNotification":
                    request= outgoingmessages.PublishFirmwareStatusNotificationRequestPayload()
                    print(request)
                else:
                    pass
            else:
                pass    
        except:
            pass    

        return request
    
    @on("ReserveNow")
    def on_reserve_now(self):
        msg_payload = args[0].payload
        print("reserve now payload", msg_payload, msg_payload["**"])
        payload
        return payload
    @after("ReserveNow")
    def after_update_firmware(self):
        self.firmwareProcedure.start()
        firmwareUpdateStart_flag = True
    

    
    @on("UpdateFirmware")
    def on_reserve_now(self):
        payload = outgoingmessages.UpdateFirmwareResponsePayload()
        return payload
    @after("UpdateFirmware")
    def after_update_firmware(self):
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
        request = incomingmessages.ReserveNowRequestPayload(id=1,expiryDateTime="03/13/2023-18:00", idToken=messagedictionary.IdToken(idToken="idtag=3 and UUID=1",type="ISO14443"))
        #await self.route_message('''[2,"83ec9e7c-378d-4317-90bd-c88d849d5158","TriggerMessage",{"requestedMessage":"Heartbeat"}]''')
        #request = outgoingmessages.BootNotificationRequestPayload(
        #    chargingStation=messagedictionary.ChargingStation(model="Wallbox XYZ",vendorName="anewone"),
        #    reason="PowerUp",
        #)
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
            self.updateStatus(), self.send_boot_notification(), self.transactionCheck()
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
     
    async def transactionCheck(self):
        global transactionOngoing
        global waitTransactionToEnd
        counter=0

        while waitTransactionToEnd:
            counter+=1
            await asyncio.sleep(1)
            if transactionOngoing == False:
                print("Transaction has ended request will occur", transactionOngoing)
                return
            
            if counter == 10 :
                transactionOngoing = False

            
        