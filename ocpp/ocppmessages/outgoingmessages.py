from dataclasses import dataclass,field
from typing import Dict, List, Optional
from .messagedictionary import *


@dataclass
class BootNotificationRequestPayload:
    chargingStation: ChargingStation
    reason: str
    customData: CustomData = field(default = None) 

@dataclass
class HeartbeatRequestPayload:
    customData: CustomData = field(default = None)

@dataclass
class AuthorizeRequestPayload:
    idtoken: IdToken
    certificate: str = field(default = None)
    iso15118CertificateHashData: List[OCSPRequestData]  = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class CancelReservationResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    

@dataclass
class CertificateSignedResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)


@dataclass
class ChangeAvailabilityResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class ClearCacheResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class ClearChargingProfileResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)    

@dataclass
class ClearDisplayMessageResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class ClearedChargingLimitRequestPayload:
    chargingLimitSource: str
    customData: CustomData = field(default = None)
    evseId: int = field(default = None)

@dataclass
class ClearVariableMonitoringResponsePayload:
    clearMonitoringResult: ClearMonitoringResult
    customData: CustomData = field(default = None)

@dataclass
class CostUpdatedResponsePayload:       
    customData: CustomData = field(default = None)

@dataclass
class CustomerInformationResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class DataTransferResponsePayload: 
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    data: Dict = field(default = None)      

@dataclass
class DeleteCertificateResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class FirmwareStatusNotificationRequestPayload:
    status: str
    customData: CustomData = field(default = None)
    requestId: int = field(default = None)

@dataclass
class Get15118EVCertificateRequestPayload:
    iso15118SchemaVersion: str
    action: str
    exiRequest: str
    customData: CustomData = field(default = None)

@dataclass
class GetBaseReportResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class GetCertificateStatusRequestPayload:
    ocspRequestData: OCSPRequestData
    customData: CustomData = field(default = None)

@dataclass
class GetChargingProfilesResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class GetCompositeScheduleResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    schedule: CompositeSchedule = field(default = None)

@dataclass
class GetDisplayMessagesResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class GetInstalledCertificateIdsResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    certificateHashDataChain: List[CertificateHashDataChain] = field(default = None)

@dataclass
class GetLocalListVersionResponsePayload:
    versionNumber: int
    customData: CustomData = field(default = None)

@dataclass
class GetLogResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    filename: str = field(default = None)

@dataclass
class GetMonitoringReportResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class GetReportResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class GetTransactionStatusResponsePayload:
    messagesInQueue: bool
    ongoingIndicator: bool = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class GetVariablesResponsePayload:
    getVariableResult: List[GetVariableResult]
    customData: CustomData = field(default = None)

@dataclass
class InstallCertificateResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class LogStatusNotificationRequestPayload:
    status: str
    customData: CustomData = field(default = None)
    requestId: int = field(default = None)

@dataclass
class MeterValuesRequestPayload:
    evseId: int
    meterValue: List[MeterValue]
    customData: CustomData = field(default = None)

@dataclass
class NotifyChargingLimitRequestPayload:
    chargingLimit: ChargingLimit
    chargingSchedule: List[ChargingSchedule] = field(default = None)
    evseId: int = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class NotifyCustomerInformationRequestPayload:
    data: str
    seqNo: int
    generatedAt: str
    requestId: int
    tbc: bool = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class NotifyDisplayMessagesRequestPayload:
    requestId: int
    tbc: bool = field(default = None)
    customData: CustomData = field(default = None)
    messageInfo: List[Message] = field(default = None)
    
@dataclass
class NotifyEVChargingNeedsRequestPayload:
    evseId: int
    chargingNeeds: ChargingNeeds
    maxScheduleTuples: int = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class NotifyEVChargingScheduleRequestPayload:
    timeBase: str
    evseId: int
    chargingSchedule: ChargingSchedule
    customData: CustomData = field(default = None)

@dataclass
class NotifyEventRequestPayload:
    generatedAt: str
    seqNo: int
    eventData: EventData
    tbc: bool = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class NotifyMonitoringReportRequestPayload:
    requestId: int
    seqNo: int
    generatedAt: str
    tbc: bool = field(default = None)
    customData: CustomData = field(default = None)
    monitor: List[MonitoringData] = field(default = None)

@dataclass
class NotifyReportRequestPayload:
    requestId: int
    generatedAt: str
    seqNo: int
    reportData: List[ReportData] = field(default = None)
    tbc: bool = field(default = None) 
    customData: CustomData = field(default = None)

@dataclass
class PublishFirmwareResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class PublishFirmwareStatusNotificationRequestPayload:
    status: str
    requestId: int = field(default = None)
    location: List[str] = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ReportChargingProfilesRequestPayload:
    requestId: int
    chargingLimitSource: str
    evseId: int
    chargingProfile: List[ChargingProfileType]
    tbc: bool = field(default = None)
    customData: CustomData = field(default = None)

@dataclass 
class RequestStartTransactionResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
    transactionId: str = field(default = None)

@dataclass
class RequestStopTransactionResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class ReservationStatusUpdateRequestPayload:
    reservationId: int
    reservationUpdateStatus: str
    customData: CustomData = field(default = None)

@dataclass
class ReserveNowResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class ResetResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SecurityEventNotificationRequestPayload:
    type: str
    timestamp: str
    techInfo: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class SendLocalListResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SetChargingProfileResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SetDisplayMessageResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SetMonitoringBaseResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SetMonitoringLevelResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SetNetworkProfileResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class SetVariableMonitoringResponsePayload:
    setMonitoringResult: List[SetMonitoringResult]
    customData: CustomData = field(default = None)

@dataclass
class SetVariablesResponsePayload:
    setVariableResult: List[SetVariableResult]
    customData: CustomData = field(default = None)

@dataclass
class SignCertificateRequestPayload:
    csr: str
    certificateType: str
    customData: CustomData = field(default = None)

@dataclass
class StatusNotificationRequestPayload:
    timestamp: str
    connectorStatus: str
    evseId: int
    connectorId: int
    customData: CustomData = field(default = None)

@dataclass
class TransactionEventRequestPayload:
    eventType: str
    timestamp: str
    triggerReason: str
    seqNo: int
    transactionInfo: TransactionInfo
    customData: CustomData = field(default = None)
    meterValue: List[MeterValue] = field(default = None)
    offline: bool = field(default = None)
    numberOfPhasesUsed: int = field(default = None)
    cableMaxCurrent: int = field(default = None)
    reservationId: int = field(default = None)
    evse: Evse = field(default = None)
    idToken: IdToken = field(default = None)

@dataclass
class TriggerMessageResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class UnlockConnectorResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)

@dataclass
class UnpublishFirmwareResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    
@dataclass
class UpdateFirmwareResponsePayload:
    status: str
    customData: CustomData = field(default = None)
    statusInfo: StatusInfo = field(default = None)
























    









