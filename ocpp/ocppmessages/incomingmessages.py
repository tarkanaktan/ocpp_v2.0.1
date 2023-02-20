from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class BootNotificationResponsePayload:
    currentTime: str
    interval: int
    status: str = field(default = "Accepted")

@dataclass 
class HeartBeatResponsePayload:
    currentTime: str

@dataclass
class AuthorizeResponsePayload:
    idTokenInfo:Dict

@dataclass
class CancelReservationRequestPayload:
    reservationId: int

@dataclass
class CertificateSignedRequestPayload:
    certificateChain: str

@dataclass
class ChangeAvailabilityRequestPayload:
    operationalStatus: str

@dataclass
class ClearCacheRequestPayload:
    pass

@dataclass
class ClearChargingProfileRequestPayload:
    pass

@dataclass
class ClearDisplayMessageRequestPayload:
    id: int

@dataclass
class ClearedChargingLimitResponsePayload:
    pass

@dataclass
class ClearVariableMonitoringRequestPayload:
    id: int

@dataclass
class CostUpdatedRequestPayload:
    totalCost: int
    transactionId: str

@dataclass
class CustomerInformationRequestPayload:
    requestId: int
    report: bool
    clear: bool

@dataclass
class DataTransferRequestPayload:
    vendorId: str

@dataclass
class DeleteCertificateRequestPayload:
    certificateHashData: Dict

@dataclass
class FirmwareStatusNotificationResponsePayload:
    pass

@dataclass
class Get15118EVCertificateResponsePayload:
    status: str
    exiResponse: str

@dataclass
class GetBaseReportRequestPayload:
    requestId: int
    reportBase: str

@dataclass
class GetCertificateStatusResponsePayload:
    status: str

@dataclass
class GetChargingProfilesRequestPayload:
    requestId: int
    chargingProfile: Dict

@dataclass
class GetCompositeScheduleRequestPayload:
    duration: int
    evseId: int

@dataclass
class GetDisplayMessagesRequestPayload:
    requestId: int

@dataclass
class GetInstalledCertificateIdsRequestPayload:
    pass

@dataclass
class GetLocalListVersionRequestPayload:
    pass

@dataclass
class GetLogRequestPayload:
    logType:  str
    requestId: int
    log: Dict
  
@dataclass
class GetMonitoringReportRequestPayload:
    requestId: int

@dataclass
class GetReportRequestPayload:
    requestId: int

@dataclass
class GetTransactionStatusRequestPayload:
    pass

@dataclass
class GetVariablesRequestPayload:
    getVariableData: Dict

@dataclass
class InstallCertificateRequestPayload:
    certificate: str
    certificateType: str
    
@dataclass
class LogStatusNotificationResponsePayload:
    pass

@dataclass
class MeterValuesResponsePayload:
    pass

@dataclass
class NotifyChargingLimitResponsePayload:
    pass

@dataclass
class NotifyCustomerInformationResponsePayload:
    pass

@dataclass
class NotifyDisplayMessagesResponsePayload:
    pass

@dataclass
class NotifyEVChargingNeedsResponsePayload:
    status: str

@dataclass
class NotifyEVChargingScheduleResponsePayload:
    status: str

@dataclass
class NotifyEventResponsePayload:
    pass

@dataclass
class NotifyMonitoringReportResponsePayload:
    pass

@dataclass
class NotifyReportRequestPayload:
    pass

@dataclass
class PublishFirmwareRequestPayload:
    location: str
    checksum: str
    requestId: int

@dataclass
class PublishFirmwareStatusNotificationResponsePayload:
    pass

@dataclass
class ReportChargingProfilesResponsePayload:
    pass

@dataclass
class RequestStartTransactionRequestPayload:
    remoteStartId: int
    idToken: Dict

@dataclass
class RequestStopTransactionRequestPayload:
    transactionId: str

@dataclass
class ReservationStatusUpdateResponsePayload:
    pass

@dataclass
class ReserveNowRequestPayload:
    id: int
    expiryDateTime: str
    idToken: Dict

@dataclass
class ResetRequestPayload:
    type: str

@dataclass
class SecurityEventNotificationResponsePayload:
    pass

@dataclass
class SendLocalListRequestPayload:
    versionNumber: int
    updateType: str

@dataclass
class SetChargingProfileRequestPayload:
    evseId: int
    chargingProfile: Dict

@dataclass
class SetDisplayMessageRequestPayload:
    message: Dict

@dataclass
class SetMonitoringBaseRequestPayload:
    monitoringBase: str

@dataclass
class SetMonitoringLevelRequestPayload:
    severity: int

@dataclass
class SetNetworkProfileRequestPayload:
    configurationSlot:int
    connectionData: Dict

@dataclass
class SetVariableMonitoringRequestPayload:
    setMonitoringData: Dict

@dataclass
class SetVariablesRequestPayload:
    setVariableData: Dict

@dataclass
class SignCertificateResponsePayload:
    status: str

@dataclass
class StatusNotificationResponsePayload:
    pass

@dataclass
class TransactionEventResponsePayload:
    pass

@dataclass
class TriggerMessageRequestPayload:
    requestedMessage: str

@dataclass
class UnlockConnectorRequestPayload:
    evseId: int
    connectorId: int

@dataclass
class UnpublishFirmwareRequestPayload:
    checksum: str

@dataclass 
class UpdateFirmwareRequestPayload:
    requestId: int
    firmware: Dict
    















        





        

    




