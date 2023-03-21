
class Reservation():
    def __init__(self,id,expirtDate,idToken,connectorType = None,evseId = None,groupIdToken = None) -> None:
        self.id = id
        self.expiryDateTime = expirtDate
        self.connectorType = connectorType
        self.evseId = evseId
        self.idToken = idToken
        self.groupIdToken = groupIdToken