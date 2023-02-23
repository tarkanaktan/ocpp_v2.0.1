from dataclasses import dataclass, field
from typing import Dict, List, Optional
from ocpp.ocppmessages.messagedictionary import *

@dataclass
class BootNotificationResponsePayload:
    currentTime: str
    interval: int
    status: str 
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass 
class HeartbeatResponsePayload:
    currentTime: str
    customData: CustomData = None

@dataclass
class AuthorizeResponsePayload:
    idTokenInfo: IdTokenInfo
    certificateStatus: str = None
    customData: CustomData = None

@dataclass
class CancelReservationRequestPayload:
    reservationId: int
    customData: CustomData = None

@dataclass
class CertificateSignedRequestPayload:
    certificateChain: str
    certificateType: str = None
    customData: CustomData = None

@dataclass
class ChangeAvailabilityRequestPayload:
    operationalStatus: str
    evse: Evse = None
    customData: CustomData = None

@dataclass
class ClearCacheRequestPayload:
    customData: CustomData = None

@dataclass
class ClearChargingProfileRequestPayload:
    customData: CustomData = None
    chargingProfileId: int = None
    chargingProfileCriteria: ClearChargingProfile = None

@dataclass
class ClearDisplayMessageRequestPayload:
    id: int
    customData: CustomData = None

@dataclass
class ClearedChargingLimitResponsePayload:
    customData: CustomData = None

@dataclass
class ClearVariableMonitoringRequestPayload:
    id: int
    customData: CustomData = None

@dataclass
class CostUpdatedRequestPayload:
    totalCost: int
    transactionId: str
    customData: CustomData = None

@dataclass
class CustomerInformationRequestPayload:
    requestId: int
    report: bool
    clear: bool
    customData: CustomData = None
    customerIdentifier: str = None
    idToken: IdToken = None
    customerCertificate: CertificateHashData = None

@dataclass
class DataTransferRequestPayload:
    vendorId: str
    customData: CustomData = None
    messageId: str = None
    data: Dict = None


@dataclass
class DeleteCertificateRequestPayload:
    certificateHashData: CertificateHashData
    customData: CustomData = None

@dataclass
class FirmwareStatusNotificationResponsePayload:
    customData: CustomData = None

@dataclass
class Get15118EVCertificateResponsePayload:
    status: str
    exiResponse: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class GetBaseReportRequestPayload:
    requestId: int
    reportBase: str
    customData: CustomData = None

@dataclass
class GetCertificateStatusResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    ocspResult: str = None

@dataclass
class GetChargingProfilesRequestPayload:
    requestId: int
    chargingProfile: ChargingProfileCriterion
    evseId: int = None
    customData: CustomData = None

@dataclass
class GetCompositeScheduleRequestPayload:
    duration: int
    evseId: int
    chargingRateUnit: str = None
    customData: CustomData = None

@dataclass
class GetDisplayMessagesRequestPayload:
    requestId: int
    customData: CustomData = None
    id: int = None
    priority: str = None
    state: str = None

@dataclass
class GetInstalledCertificateIdsRequestPayload:
    customData: CustomData = None
    certificateType: List[str] = None

@dataclass
class GetLocalListVersionRequestPayload:
    customData: CustomData = None

@dataclass
class GetLogRequestPayload:
    logType:  str
    requestId: int
    log: Log
    customData: CustomData = None
    retries: int = None
    retryInterval: int = None

@dataclass
class GetMonitoringReportRequestPayload:
    requestId: int
    customData: CustomData = None
    componentVariable: List[ComponentVariable] = None
    monitoringCriteria: List[str] = None

@dataclass
class GetReportRequestPayload:
    requestId: int
    customData: CustomData = None
    componentVariable: List[ComponentVariable] = None
    componentCriteria: List[str] = None

@dataclass
class GetTransactionStatusRequestPayload:
    customData: CustomData = None
    transactionId: str = None

@dataclass
class GetVariablesRequestPayload:
    getVariableData: GetVariableData
    customData: CustomData = None

@dataclass
class InstallCertificateRequestPayload:
    certificate: str
    certificateType: str
    customData: CustomData = None
    
@dataclass
class LogStatusNotificationResponsePayload:
    customData: CustomData = None

@dataclass
class MeterValuesResponsePayload:
    customData: CustomData = None

@dataclass
class NotifyChargingLimitResponsePayload:
    customData: CustomData = None

@dataclass
class NotifyCustomerInformationResponsePayload:
    customData: CustomData = None

@dataclass
class NotifyDisplayMessagesResponsePayload:
    customData: CustomData = None

@dataclass
class NotifyEVChargingNeedsResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class NotifyEVChargingScheduleResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class NotifyEventResponsePayload:
    customData: CustomData = None

@dataclass
class NotifyMonitoringReportResponsePayload:
    customData: CustomData = None

@dataclass
class NotifyReportRequestPayload:
    customData: CustomData = None

@dataclass
class PublishFirmwareRequestPayload:
    location: str
    checksum: str
    requestId: int
    customData: CustomData = None
    retries: int = None
    retryInterval: int = None

@dataclass
class PublishFirmwareStatusNotificationResponsePayload:
    customData: CustomData = None

@dataclass
class ReportChargingProfilesResponsePayload:
    customData: CustomData = None

@dataclass
class RequestStartTransactionRequestPayload:
    remoteStartId: int
    idToken: IdToken
    customData: CustomData = None
    evseId: int = None
    groupIdToken: IdToken = None
    chargingProfile: ChargingProfileType = None


@dataclass
class RequestStopTransactionRequestPayload:
    transactionId: str
    customData: CustomData = None

@dataclass
class ReservationStatusUpdateResponsePayload:
    customData: CustomData = None

@dataclass
class ReserveNowRequestPayload:
    id: int
    expiryDateTime: str
    idToken: IdToken
    customData: CustomData = None
    evseId: int = None
    groupIdToken: IdToken = None
    connectorType: str = None

@dataclass
class ResetRequestPayload:
    type: str
    customData: CustomData = None
    evseId: int = None

@dataclass
class SecurityEventNotificationResponsePayload:
    customData: CustomData = None

@dataclass
class SendLocalListRequestPayload:
    versionNumber: int
    updateType: str
    customData: CustomData = None
    localAuthorizationList: List[AuthorizationData] = None

@dataclass
class SetChargingProfileRequestPayload:
    evseId: int
    chargingProfile: ChargingProfileType
    customData: CustomData = None

@dataclass
class SetDisplayMessageRequestPayload:
    message: Message
    customData: CustomData = None

@dataclass
class SetMonitoringBaseRequestPayload:
    monitoringBase: str
    customData: CustomData = None

@dataclass
class SetMonitoringLevelRequestPayload:
    severity: int
    customData: CustomData = None

@dataclass
class SetNetworkProfileRequestPayload:
    configurationSlot:int
    connectionData: ConnectionData
    customData: CustomData = None

@dataclass
class SetVariableMonitoringRequestPayload:
    setMonitoringData: List[SetMonitoringData]
    customData: CustomData = None

@dataclass
class SetVariablesRequestPayload:
    setVariableData: List[SetVariableData]
    customData: CustomData = None

@dataclass
class SignCertificateResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class StatusNotificationResponsePayload:
    customData: CustomData = None

@dataclass
class TransactionEventResponsePayload:
    customData: CustomData = None
    totalCost: int = None
    chargingPriority: int = None
    idTokenInfo: IdTokenInfo = None
    updatedPersonalMessage: MessageContentType = None

@dataclass
class TriggerMessageRequestPayload:
    requestedMessage: str
    customData: CustomData = None
    evse: Evse = None

@dataclass
class UnlockConnectorRequestPayload:
    evseId: int
    connectorId: int
    customData: CustomData = None

@dataclass
class UnpublishFirmwareRequestPayload:
    checksum: str
    customData: CustomData = None

@dataclass 
class UpdateFirmwareRequestPayload:
    requestId: int
    firmware: Firmware
    customData: CustomData = None
    retryInterval: int = None
    retries: int = None



    















        





        

    




