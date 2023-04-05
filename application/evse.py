from datetime import datetime

import ocpp.ocppmessages.outgoingmessages as outgoingmessages
from application.enumtypes import *

class Evse():
    def __init__(self,id) -> None:
        self.connectorId = id
        self.status = None
        self.reservation = None
        self.transaction = None
        self.operation = None

    def setStatus(self,status):
        self.status = status

    def getStatus(self):
        return self.status

    def setReservation(self,reservation):
        self.reservation = reservation

    def getReservation(self):
        return self.reservation

    def setTransaction(self,transaction):
        self.transaction = transaction

    def getTransaction(self):
        return self.transaction

    async def evseControl(self,cp):
        await self.reservationControl(cp)

    async def reservationControl(self,cp):
        if self.reservation is None:
            return
        
        expiryDateConverted = datetime.strptime(self.reservation.expiryDateTime,'%Y-%m-%dT%H:%M:%S.%f')
        timeNow = datetime.now()
        print("evse control",expiryDateConverted,timeNow)
        if self.status == ConnectorStatusEnumType.Faulted:
            
            payload = outgoingmessages.ReservationStatusUpdateRequestPayload(reservationId=self.reservation.id,reservationUpdateStatus=ReservationUpdateStatusEnumType.Removed)
            print(payload)
            await cp.call(payload)
            self.reservation = None

        if timeNow > expiryDateConverted:
            
            payload = outgoingmessages.ReservationStatusUpdateRequestPayload(reservationId=self.reservation.id,reservationUpdateStatus=ReservationUpdateStatusEnumType.Expired)
            #TODO self.status = actual_state
            self.status = ConnectorStatusEnumType.Available
            print(payload)
            await cp.call(payload)
            self.reservation = None
        
        
