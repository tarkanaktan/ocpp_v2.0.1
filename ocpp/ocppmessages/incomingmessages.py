from dataclasses import dataclass, field
from typing import Dict, List, Optional
from ocpp.ocppmessages.messagedictionary import *

@dataclass
class BootNotificationResponsePayload:
    currentTime: str
    interval: int
    status: str 
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass 
class HeartbeatResponsePayload:
    currentTime: str
    customData: CustomData = field(default = None)

@dataclass
class AuthorizeResponsePayload:
    idTokenInfo: IdTokenInfo
    certificateStatus: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class CancelReservationRequestPayload:
    reservationId: int
    customData: CustomData = field(default = None)

@dataclass
class CertificateSignedRequestPayload:
    certificateChain: str
    certificateType: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ChangeAvailabilityRequestPayload:
    operationalStatus: str
    evse: Evse = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ClearCacheRequestPayload:
    customData: CustomData = field(default = None)

@dataclass
class ClearChargingProfileRequestPayload:
    customData: CustomData = field(default = None)
    chargingProfileId: int = field(default = None)
    chargingProfileCriteria: ClearChargingProfile = field(default = None)

@dataclass
class ClearDisplayMessageRequestPayload:
    id: int
    customData: CustomData = field(default = None)

@dataclass
class ClearedChargingLimitResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class ClearVariableMonitoringRequestPayload:
    id: int
    customData: CustomData = field(default = None)

@dataclass
class CostUpdatedRequestPayload:
    totalCost: int
    transactionId: str
    customData: CustomData = field(default = None)

@dataclass
class CustomerInformationRequestPayload:
    requestId: int
    report: bool
    clear: bool
    customData: CustomData = field(default = None)
    customerIdentifier: str = field(default = None)
    idToken: IdToken = field(default = None)
    customerCertificate: CertificateHashData = field(default = None)

@dataclass
class DataTransferRequestPayload:
    vendorId: str
    customData: CustomData = field(default = None)
    messageId: str = field(default = None)
    data: Dict = field(default = None)


@dataclass
class DeleteCertificateRequestPayload:
    certificateHashData: CertificateHashData
    customData: CustomData = field(default = None)

@dataclass
class FirmwareStatusNotificationResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class Get15118EVCertificateResponsePayload:
    status: str
    exiResponse: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class GetBaseReportRequestPayload:
    requestId: int
    reportBase: str
    customData: CustomData = field(default = None)

@dataclass
class GetCertificateStatusResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    ocspResult: str = field(default = None)

@dataclass
class GetChargingProfilesRequestPayload:
    requestId: int
    chargingProfile: ChargingProfileCriterion
    evseId: int = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class GetCompositeScheduleRequestPayload:
    duration: int
    evseId: int
    chargingRateUnit: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class GetDisplayMessagesRequestPayload:
    requestId: int
    customData: CustomData = field(default = None)
    id: int = field(default = None)
    priority: str = field(default = None)
    state: str = field(default = None)

@dataclass
class GetInstalledCertificateIdsRequestPayload:
    customData: CustomData = field(default = None)
    certificateType: List[str] = field(default = None)

@dataclass
class GetLocalListVersionRequestPayload:
    customData: CustomData = field(default = None)

@dataclass
class GetLogRequestPayload:
    logType:  str
    requestId: int
    log: Log
    customData: CustomData = field(default = None)
    retries: int = field(default = None)
    retryInterval: int = field(default = None)

@dataclass
class GetMonitoringReportRequestPayload:
    requestId: int
    customData: CustomData = field(default = None)
    componentVariable: List[ComponentVariable] = field(default = None)
    monitoringCriteria: List[str] = field(default = None)

@dataclass
class GetReportRequestPayload:
    requestId: int
    customData: CustomData = field(default = None)
    componentVariable: List[ComponentVariable] = field(default = None)
    componentCriteria: List[str] = field(default = None)

@dataclass
class GetTransactionStatusRequestPayload:
    customData: CustomData = field(default = None)
    transactionId: str = field(default = None)

@dataclass
class GetVariablesRequestPayload:
    getVariableData: GetVariableData
    customData: CustomData = field(default = None)

@dataclass
class InstallCertificateRequestPayload:
    certificate: str
    certificateType: str
    customData: CustomData = field(default = None)
    
@dataclass
class LogStatusNotificationResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class MeterValuesResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class NotifyChargingLimitResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class NotifyCustomerInformationResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class NotifyDisplayMessagesResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class NotifyEVChargingNeedsResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class NotifyEVChargingScheduleResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class NotifyEventResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class NotifyMonitoringReportResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class NotifyReportRequestPayload:
    customData: CustomData = field(default = None)

@dataclass
class PublishFirmwareRequestPayload:
    location: str
    checksum: str
    requestId: int
    customData: CustomData = field(default = None)
    retries: int = field(default = None)
    retryInterval: int = field(default = None)

@dataclass
class PublishFirmwareStatusNotificationResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class ReportChargingProfilesResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class RequestStartTransactionRequestPayload:
    remoteStartId: int
    idToken: IdToken
    customData: CustomData = field(default = None)
    evseId: int = field(default = None)
    groupIdToken: IdToken = field(default = None)
    chargingProfile: ChargingProfileType = field(default = None)


@dataclass
class RequestStopTransactionRequestPayload:
    transactionId: str
    customData: CustomData = field(default = None)

@dataclass
class ReservationStatusUpdateResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class ReserveNowRequestPayload:
    id: int
    expiryDateTime: str
    idToken: IdToken
    customData: CustomData = field(default = None)
    evseId: int = field(default = None)
    groupIdToken: IdToken = field(default = None)
    connectorType: str = field(default = None)

@dataclass
class ResetRequestPayload:
    type: str
    customData: CustomData = field(default = None)
    evseId: int = field(default = None)

@dataclass
class SecurityEventNotificationResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class SendLocalListRequestPayload:
    versionNumber: int
    updateType: str
    customData: CustomData = field(default = None)
    localAuthorizationList: List[AuthorizationData] = field(default = None)

@dataclass
class SetChargingProfileRequestPayload:
    evseId: int
    chargingProfile: ChargingProfileType
    customData: CustomData = field(default = None)

@dataclass
class SetDisplayMessageRequestPayload:
    message: Message
    customData: CustomData = field(default = None)

@dataclass
class SetMonitoringBaseRequestPayload:
    monitoringBase: str
    customData: CustomData = field(default = None)

@dataclass
class SetMonitoringLevelRequestPayload:
    severity: int
    customData: CustomData = field(default = None)

@dataclass
class SetNetworkProfileRequestPayload:
    configurationSlot:int
    connectionData: ConnectionData
    customData: CustomData = field(default = None)

@dataclass
class SetVariableMonitoringRequestPayload:
    setMonitoringData: List[SetMonitoringData]
    customData: CustomData = field(default = None)

@dataclass
class SetVariablesRequestPayload:
    setVariableData: List[SetVariableData]
    customData: CustomData = field(default = None)

@dataclass
class SignCertificateResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class StatusNotificationResponsePayload:
    customData: CustomData = field(default = None)

@dataclass
class TransactionEventResponsePayload:
    customData: CustomData = field(default = None)
    totalCost: int = field(default = None)
    chargingPriority: int = field(default = None)
    idTokenInfo: IdTokenInfo = field(default = None)
    updatedPersonalMessage: MessageContentType = field(default = None)

@dataclass
class TriggerMessageRequestPayload:
    requestedMessage: str
    customData: CustomData = field(default = None)
    evse: Evse = field(default = None)

@dataclass
class UnlockConnectorRequestPayload:
    evseId: int
    connectorId: int
    customData: CustomData = field(default = None)

@dataclass
class UnpublishFirmwareRequestPayload:
    checksum: str
    customData: CustomData = field(default = None)

@dataclass 
class UpdateFirmwareRequestPayload:
    requestId: int
    firmware: Firmware
    customData: CustomData = field(default = None)
    retryInterval: int = field(default = None)
    retries: int = field(default = None)



    















        





        

    




