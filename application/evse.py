from application.enumtypes import *

class Evse():
    def __init__(self,id) -> None:
        self.connectorId = id
        self.status = None
        self.reservation = None
        self.transaction = None

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