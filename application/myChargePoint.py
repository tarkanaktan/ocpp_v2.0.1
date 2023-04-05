import asyncio
import random
import json
from dataclasses import asdict
from datetime import datetime
from ocpp.chargepoint import ChargePoint, LOGGER
from ocpp.routing import onresponse,on,after
import ocpp.ocppmessages.incomingmessages as incomingmessages
import ocpp.ocppmessages.outgoingmessages as outgoingmessages
import ocpp.ocppmessages.messagedictionary as messagedictionary
from application.reservation import Reservation

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
    @on("SetVariables")
    async def on_setVariables(self,*args):
        payload = args[0].payload
        resultList = []
        setVariableData = payload["setVariableData"]
        for variable in setVariableData:
            try:
                attributeType = variable["attributeType"]
            except:
                attributeType = None
            try:
                attributeType = variable["attributeType"]
            except:
                attributeType = None
            try:
                componentInstance = variable["component"]["instance"]
            except:
                componentInstance = None
            try:
                variableInstance = variable["variable"]["instance"]
            except:
                variableInstance = None
            value = variable["attributeValue"]
            attributeStatus = await self.variables.checkAttributeStatus(variable,value)
            componentData = outgoingmessages.Component(name=variable["component"]["name"],instance=componentInstance)
            variableData = outgoingmessages.Variable(name=variable["variable"]["name"],instance=variableInstance)
            result = outgoingmessages.SetVariableResult(attributeStatus=attributeStatus,component=asdict(componentData),variable=asdict(variableData),attributeType= attributeType)
            resultList.append(result)
        response = outgoingmessages.SetVariablesResponsePayload(setVariableResult=resultList)
        return response

    @on("GetVariables")
    async def on_getVariables(self,*args):
        payload = args[0].payload
        resultList =[]
        getVariableData = payload["getVariableData"]
        for variable in getVariableData:
            try:
                attributeType = variable["attributeType"]
            except:
                attributeType = None
            try:
                componentInstance = variable["component"]["instance"]
            except:
                componentInstance = None
            try:
                variableInstance = variable["variable"]["instance"]
            except:
                variableInstance = None
            componentData = outgoingmessages.Component(name=variable["component"]["name"],instance=componentInstance)
            variableData = outgoingmessages.Variable(name=variable["variable"]["name"],instance=variableInstance)
            attrValue = await self.variables.getAttributeValue(variable)#attrValue contins value and attrStatus
            result = outgoingmessages.GetVariableResult(attributeStatus=attrValue[1],attributeValue=attrValue[0],component=componentData,variable=variableData)
            resultList.append(result)
        response = outgoingmessages.GetVariablesResponsePayload(getVariableResult=resultList)
        return response

    @on("GetBaseReport")
    def on_getBaseReport(self,*args):
        payload = args[0].payload
        response = outgoingmessages.GetBaseReportResponsePayload(GenericDeviceModelStatusEnumType.Accepted)
        return response

    @after("GetBaseReport")
    async def after_getBaseReport(self,*args):
        payload = args[1].payload
        reportBase = payload["reportBase"]
        requestId = payload["requestId"]
        seqNo = 0
        request = outgoingmessages.NotifyReportRequestPayload(requestId=requestId,generatedAt=datetime.utcnow().isoformat(),seqNo=seqNo)
        await self.call(request)
    
    @on("GetReport")
    def on_getBaseReport(self,*args):
        payload = args[0].payload
        requestId = payload["requestId"]
        try:
            componentCriteria = payload["componentCriteria"]
        except:
            componentCriteria = None
        try:
            componentVariable = payload["componentVariable"]
        except:
            componentVariable = None
    
    @on("SetNetworkProfile")
    async def on_setNetworkProfile(self,*args):
        payload = args[0].payload
        connectionData = payload["connectionData"] #TODO store this data
        configurationSlot = payload["configurationSlot"]
        if(connectionData["ocppVersion"] != OCPPVersionEnumType.OCPP20 or connectionData["ocppTransport"] != OCPPTransportEnumType.JSON):
            response = outgoingmessages.SetNetworkProfileResponsePayload(status=SetNetworkProfileStatusEnumType.Rejected)
            return response
        if(int(connectionData["securityProfile"]) < int(self.variables.SecurityProfile)):
            response = outgoingmessages.SetNetworkProfileResponsePayload(status=SetNetworkProfileStatusEnumType.Rejected)
            return response
        try:
            await self.variables.putNetworkProfile(configurationSlot,str(connectionData))
        except:
            response = outgoingmessages.SetNetworkProfileResponsePayload(status=SetNetworkProfileStatusEnumType.Failed)
            return response
        response = outgoingmessages.SetNetworkProfileResponsePayload(status=SetNetworkProfileStatusEnumType.Accepted)
        return response

#Change Availability: It enables the CSMS to change the availability of an EVSE or Connector or Charging Station to Operative or Inoperative 
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
    def on_reserve_now(self,*args):
        global actual_state
        msg_payload = args[0].payload
        try:
            evseId = msg_payload["evseId"]
        except:
            evseId = None
        try:
            connectorType = msg_payload["connectorType"]
        except:
            connectorType = None
        try:
            groupIdToken = msg_payload["groupIdToken"]
        except:
            groupIdToken = None
        print("reserve now payload", msg_payload)
        if self.variables.ReservationEnabled is True:
            if evseId is None:
                for i in range(1,3):
                    if self.evseList[i].reservation is None and self.evseList[i].status == ConnectorStatusEnumType.Faulted:
                        payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Faulted)
                    elif self.evseList[i].reservation is None and self.evseList[i].status == ConnectorStatusEnumType.Available:
                        reservation = Reservation(msg_payload["id"],msg_payload["expiryDateTime"],msg_payload["idToken"])
                        self.evseList[i].setReservation(reservation)
                        print(self.evseList[i].connectorId)
                        payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Accepted)
                        #actual_state = ConnectorStatusEnumType.Reserved
                        self.evseList[i].status = ConnectorStatusEnumType.Reserved
                        break
                    else:
                        payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Occupied)
            else:
                for evse in self.evseList:
                    if(msg_payload["evseId"] == evse.connectorId and evse.reservation is None):
                        reservation = Reservation(msg_payload["id"],msg_payload["expiryDateTime"],msg_payload["idToken"],msg_payload["evseId"])
                        evse.setReservation(reservation)
                        payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Accepted)
                        #actual_state = ConnectorStatusEnumType.Reserved
                        self.evseList[i].status = ConnectorStatusEnumType.Reserved
                        break
                    elif (msg_payload["evseId"] == evse.connectorId and evse.status == ConnectorStatusEnumType.Faulted):
                        payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Faulted)

                    elif (msg_payload["evseId"] == evse.connectorId and evse.reservation is not None):
                        payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Occupied)
        else:
            payload = outgoingmessages.ReserveNowResponsePayload(ReserveNowStatusEnumType.Rejected)
        return payload

    async def send_heartbeat(self, interval):
        request = outgoingmessages.HeartbeatRequestPayload()
        while True:
            global actual_state
            await self.call(request)
            await asyncio.sleep(2)
            await self.route_message('''[2,"cda5d782-dfe2-4f44-a946-405bc76dab72","ReserveNow",{"id":1,"expiryDateTime":"2023-03-20T11:38:44.094356","idToken":{"idToken":"12345678","type":"ISO14443"}}]''')
            await asyncio.sleep(1)
            await self.route_message('''[2,"asd5d782-dfe2-4f44-a946-405bc76dab72","ReserveNow",{"id":2,"expiryDateTime":"2023-03-20T11:38:44.094356","idToken":{"idToken":"asdfghjk","type":"ISO14443"}}]''')
            await asyncio.sleep(1)
            await self.route_message('''[2,"asd12345-dfe2-4f44-a946-405bc76dab72","ReserveNow",{"id":3,"expiryDateTime":"2023-03-20T11:38:44.094356","idToken":{"idToken":"1232asda","type":"ISO14443"}}]''')            
            await asyncio.sleep(1)
            random_attr = random.choice(ConnectorStatusEnumType.attrlist)
            actual_state = getattr(ConnectorStatusEnumType,random_attr)
            await asyncio.sleep(interval - 5)

    async def send_boot_notification(self):
        idtoken = incomingmessages.IdToken(idToken="12345678",type=IdTokenEnumType.ISO14443)
        req = incomingmessages.ReserveNowRequestPayload(id=1,expiryDateTime=datetime.utcnow().isoformat(), idToken=idtoken)
        #await self.call(req)
        await self.route_message('''[2,"885da9cf-86bd-4a24-b8a4-de990a818226","SetVariables",{"setVariableData":[{"attributeValue":180,"component":{"name":"OCPPCommCtrlr"},"variable":{"name":"HeartbeatInterval"}},{"attributeValue":"True","component":{"name":"ReservationCtrlr"},"variable":{"name":"Enabled"}}]}] ''')
        #await self.route_message('''[2,"30902697-03ef-4754-9ba4-6f8dd109ddf7","GetVariables",{"getVariableData":[{"component":{"name":"OCPPCommCtrlr"},"variable":{"name":"HeartbeatInterval"}},{"component":{"name":"DeviceDataCtrlr"},"variable":{"name":"ItemsPerMessage","instance":"GetVariables"}}]}]''')
        request = outgoingmessages.BootNotificationRequestPayload(
            chargingStation=messagedictionary.ChargingStation(model="Wallbox XYZ",vendorName="anewone"),
            reason="PowerUp",
        )
        try:
            response = await self.call(request)
            if response.status == RegistrationStatusEnumType.Accepted:
                self.logger.info("Connected to central system.")
                self.online = True
                #await self.variables.setVariable("HeartbeatInterval",response.interval)
                print(self.variables.HeartbeatInterval)
                await self.send_heartbeat(response.interval)
            elif response.status == RegistrationStatusEnumType.Pending or response.status == RegistrationStatusEnumType.Rejected:
                self.logger.info("Pending received trying to reconnect to central system.")
                await asyncio.sleep(response.interval)
                await self.send_boot_notification()
        except Exception as e:
            print(e)
    
    async def startProcedure(self):
        await asyncio.gather(
            self.updateStatus(), self.send_boot_notification(), self.transactionCheck(),self.evseHandler()
        )

    async def updateStatus(self):
        global actual_state
        timer = 0
        previousOperationList = []
        previousStateList = []
        for evse in self.evseList:
            evse.status = ConnectorStatusEnumType.Available
            evse.operation = OperationalStatusEnumType.Operative
            previousStateList.append(ConnectorStatusEnumType.Uninitialized)
            previousOperationList.append(OperationalStatusEnumType.Operative)
        actual_state = ConnectorStatusEnumType.Uninitialized
        while True:
            for i in range(self.connectorCount+1):
                if(previousStateList[i] != self.evseList[i].status and self.online is True):
                    previousStateList[i] = self.evseList[i].status
                    request = outgoingmessages.StatusNotificationRequestPayload(timestamp=datetime.utcnow().isoformat(),connectorStatus=self.evseList[i].status,evseId=self.evseList[i].connectorId,connectorId=self.evseList[i].connectorId)
                    await self.call(request)
                elif(previousOperationList[i] != self.evseList[i].operation and self.online is True):
                    if waitTransactionToEnd is False:
                        previousOperationList[i] = self.evseList[i].operation
                        if(self.evseList[i].operation == "Operative"):
                            request = outgoingmessages.StatusNotificationRequestPayload(timestamp=datetime.utcnow().isoformat(),connectorStatus=self.evseList[i].status,evseId=self.evseList[i].connectorId,connectorId=self.evseList[i].connectorId)
                        elif(self.evseList[i].operation == "InOperative" and self.evseList[i].status == ConnectorStatusEnumType.Faulted):
                            request = outgoingmessages.StatusNotificationRequestPayload(timestamp=datetime.utcnow().isoformat(),connectorStatus=self.evseList[i].status,evseId=self.evseList[i].connectorId,connectorId=self.evseList[i].connectorId)
                        else:
                            self.evseList[i].status = ConnectorStatusEnumType.Unavailable
                            previousStateList[i] = self.evseList[i].status
                            request = outgoingmessages.StatusNotificationRequestPayload(timestamp=datetime.utcnow().isoformat(),connectorStatus=ConnectorStatusEnumType.Unavailable,evseId=self.evseList[i].connectorId,connectorId=self.evseList[i].connectorId)
                        await self.call(request)
                    else:
                        pass
                elif(timer >= self.variables.OfflineThreshold and self.online is False):
                    timer = 0
                    request = outgoingmessages.StatusNotificationRequestPayload(timestamp=datetime.utcnow().isoformat(),connectorStatus=self.evseList[i].status,evseId=self.evseList[i].connectorId,connectorId=self.evseList[i].connectorId) #TODO offline behaviour will be added
            await asyncio.sleep(1)
            timer = timer + 1
    
    async def evseHandler(self):
        while True:
            for evse in self.evseList:
                await evse.evseControl(self)
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
                waitTransactionToEnd = False
                return
            
            if counter == 10 :
                transactionOngoing = False

            
        
