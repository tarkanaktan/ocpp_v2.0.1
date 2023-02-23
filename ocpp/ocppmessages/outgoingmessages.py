from dataclasses import dataclass,field
from typing import Dict, List, Optional
from ocpp.ocppmessages.messagedictionary import *


@dataclass
class BootNotificationRequestPayload:
    chargingStation: ChargingStation
    reason: str
    customData: CustomData = None

@dataclass
class HeartbeatRequestPayload:
    customData: CustomData = None

@dataclass
class AuthorizeRequestPayload:
    idtoken: IdToken
    certificate: str = None
    iso15118CertificateHashData: List[OCSPRequestData]  = None
    customData: CustomData = None

@dataclass
class CancelReservationResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    

@dataclass
class CertificateSignedResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None


@dataclass
class ChangeAvailabilityResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class ClearCacheResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class ClearChargingProfileResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None    

@dataclass
class ClearDisplayMessageResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class ClearedChargingLimitRequestPayload:
    chargingLimitSource: str
    customData: CustomData = None
    evseId: int = None

@dataclass
class ClearVariableMonitoringResponsePayload:
    clearMonitoringResult: ClearMonitoringResult
    customData: CustomData = None

@dataclass
class CostUpdatedResponsePayload:       
    customData: CustomData = None

@dataclass
class CustomerInformationResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class DataTransferResponsePayload: 
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    data: Dict = None      

@dataclass
class DeleteCertificateResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class FirmwareStatusNotificationRequestPayload:
    status: str
    customData: CustomData = None
    requestId: int = None

@dataclass
class Get15118EVCertificateRequestPayload:
    iso15118SchemaVersion: str
    action: str
    exiRequest: str
    customData: CustomData = None

@dataclass
class GetBaseReportResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class GetCertificateStatusRequestPayload:
    ocspRequestData: OCSPRequestData
    customData: CustomData = None

@dataclass
class GetChargingProfilesResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class GetCompositeScheduleResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    schedule: CompositeSchedule = None

@dataclass
class GetDisplayMessagesResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class GetInstalledCertificateIdsResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    certificateHashDataChain: List[CertificateHashDataChain] = None

@dataclass
class GetLocalListVersionResponsePayload:
    versionNumber: int
    customData: CustomData = None

@dataclass
class GetLogResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    filename: str = None

@dataclass
class GetMonitoringReportResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class GetReportResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class GetTransactionStatusResponsePayload:
    messagesInQueue: bool
    ongoingIndicator: bool = None
    customData: CustomData = None

@dataclass
class GetVariablesResponsePayload:
    getVariableResult: List[GetVariableResult]
    customData: CustomData = None

@dataclass
class InstallCertificateResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class LogStatusNotificationRequestPayload:
    status: str
    customData: CustomData = None
    requestId: int = None

@dataclass
class MeterValuesRequestPayload:
    evseId: int
    meterValue: List[MeterValue]
    customData: CustomData = None

@dataclass
class NotifyChargingLimitRequestPayload:
    chargingLimit: ChargingLimit
    chargingSchedule: List[ChargingSchedule] = None
    evseId: int = None
    customData: CustomData = None

@dataclass
class NotifyCustomerInformationRequestPayload:
    data: str
    seqNo: int
    generatedAt: str
    requestId: int
    tbc: bool = None
    customData: CustomData = None

@dataclass
class NotifyDisplayMessagesRequestPayload:
    requestId: int
    tbc: bool = None
    customData: CustomData = None
    messageInfo: List[Message] = None
    
@dataclass
class NotifyEVChargingNeedsRequestPayload:
    evseId: int
    chargingNeeds: ChargingNeeds
    maxScheduleTuples: int = None
    customData: CustomData = None

@dataclass
class NotifyEVChargingScheduleRequestPayload:
    timeBase: str
    evseId: int
    chargingSchedule: ChargingSchedule
    customData: CustomData = None

@dataclass
class NotifyEventRequestPayload:
    generatedAt: str
    seqNo: int
    eventData: EventData
    tbc: bool = None
    customData: CustomData = None

@dataclass
class NotifyMonitoringReportRequestPayload:
    requestId: int
    seqNo: int
    generatedAt: str
    tbc: bool = None
    customData: CustomData = None
    monitor: List[MonitoringData] = None

@dataclass
class NotifyReportRequestPayload:
    requestId: int
    generatedAt: str
    seqNo: int
    reportData: List[ReportData] = None
    tbc: bool = None 
    customData: CustomData = None

@dataclass
class PublishFirmwareResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class PublishFirmwareStatusNotificationRequestPayload:
    status: str
    requestId: int = None
    location: List[str] = None
    customData: CustomData = None

@dataclass
class ReportChargingProfilesRequestPayload:
    requestId: int
    chargingLimitSource: str
    evseId: int
    chargingProfile: List[ChargingProfileType]
    tbc: bool = None
    customData: CustomData = None

@dataclass 
class RequestStartTransactionResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
    transactionId: str = None

@dataclass
class RequestStopTransactionResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class ReservationStatusUpdateRequestPayload:
    reservationId: int
    reservationUpdateStatus: str
    customData: CustomData = None

@dataclass
class ReserveNowResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class ResetResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SecurityEventNotificationRequestPayload:
    type: str
    timestamp: str
    techInfo: str = None
    customData: CustomData = None

@dataclass
class SendLocalListResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SetChargingProfileResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SetDisplayMessageResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SetMonitoringBaseResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SetMonitoringLevelResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SetNetworkProfileResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class SetVariableMonitoringResponsePayload:
    setMonitoringResult: List[SetMonitoringResult]
    customData: CustomData = None

@dataclass
class SetVariablesResponsePayload:
    setVariableResult: List[SetVariableResult]
    customData: CustomData = None

@dataclass
class SignCertificateRequestPayload:
    csr: str
    certificateType: str
    customData: CustomData = None

@dataclass
class StatusNotificationRequestPayload:
    timestamp: str
    connectorStatus: str
    evseId: int
    connectorId: int
    customData: CustomData = None

@dataclass
class TransactionEventRequestPayload:
    eventType: str
    timestamp: str
    triggerReason: str
    seqNo: int
    transactionInfo: TransactionInfo
    customData: CustomData = None
    meterValue: List[MeterValue] = None
    offline: bool = None
    numberOfPhasesUsed: int = None
    cableMaxCurrent: int = None
    reservationId: int = None
    evse: Evse = None
    idToken: IdToken = None

@dataclass
class TriggerMessageResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class UnlockConnectorResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None

@dataclass
class UnpublishFirmwareResponsePayload:
    status: str
    customData: CustomData = None
    
@dataclass
class UpdateFirmwareResponsePayload:
    status: str
    customData: CustomData = None
    statusInfo: StatusInfo = None
























    









