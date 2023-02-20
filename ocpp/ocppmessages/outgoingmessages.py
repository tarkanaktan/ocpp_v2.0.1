from dataclasses import dataclass,field
from typing import Dict, List, Optional


@dataclass
class BootNotificationRequestPayload:
    chargingStation: Dict
    reason: str = field(default = "PowerUp")

@dataclass
class HeartbeatRequestPayload:
    pass

@dataclass
class AuthorizeRequestPayload:
    idtoken: Dict

@dataclass
class CancelReservationResponsePayload:
    status: str

@dataclass
class CertificateSignedResponsePayload:
    status: str

@dataclass
class ChangeAvailabilityResponsePayload:
    status: str

@dataclass
class ClearCacheResponsePayload:
    status: str

@dataclass
class ClearChargingProfileResponsePayload:
    status: str

@dataclass
class ClearDisplayMessageResponsePayload:
    status: str

@dataclass
class ClearedChargingLimitRequestPayload:
    chargingLimitSource: str

@dataclass
class ClearVariableMonitoringResponsePayload:
    clearMonitoringResult: Dict

@dataclass
class CostUpdatedResponsePayload:       
    pass

@dataclass
class CustomerInformationResponsePayload:
    status: str

@dataclass
class DataTransferResponsePayload: 
    status: str   

@dataclass
class DeleteCertificateResponsePayload:
    status: str

@dataclass
class FirmwareStatusNotificationRequestPayload:
    status: str

@dataclass
class Get15118EVCertificateRequestPayload:
    iso15118SchemaVersion: str
    action: str
    exiRequest: str

@dataclass
class GetBaseReportResponsePayload:
    status: str

@dataclass
class GetCertificateStatusRequestPayload:
    ocspRequestData: Dict

@dataclass
class GetChargingProfilesResponsePayload:
    status: str

@dataclass
class GetCompositeScheduleResponsePayload:
    status: str

@dataclass
class GetDisplayMessagesResponsePayload:
    status: str

@dataclass
class GetInstalledCertificateIdsResponsePayload:
    status: str

@dataclass
class GetLocalListVersionResponsePayload:
    versionNumber: int

@dataclass
class GetLogResponsePayload:
    status: str

@dataclass
class GetMonitoringReportResponsePayload:
    status: str

@dataclass
class GetReportResponsePayload:
    status: str

@dataclass
class GetTransactionStatusResponsePayload:
    messagesInQueue: bool

@dataclass
class GetVariablesResponsePayload:
    getVariableResult: Dict

@dataclass
class InstallCertificateResponsePayload:
    status: str

@dataclass
class LogStatusNotificationRequestPayload:
    status: str

@dataclass
class MeterValuesRequestPayload:
    evseId: int
    meterValue: Dict

@dataclass
class NotifyChargingLimitRequestPayload:
    chargingLimit: Dict

@dataclass
class NotifyCustomerInformationRequestPayload:
    data: str
    seqNo: int
    generatedAt: str
    requestId: int

@dataclass
class NotifyDisplayMessagesRequestPayload:
    requestId: int

@dataclass
class NotifyEVChargingNeedsRequestPayload:
    evseId: int
    chargingNeeds: Dict

@dataclass
class NotifyEVChargingScheduleRequestPayload:
    timeBase: str
    evseId: int
    chargingSchedule: Dict

@dataclass
class NotifyEventRequestPayload:
    generatedAt: str
    seqNo: int
    eventData: Dict

@dataclass
class NotifyMonitoringReportRequestPayload:
    requestId: int
    seqNo: int
    generatedAt: str

@dataclass
class NotifyReportRequestPayload:
    requestId: int
    generatedAt: str
    seqNo: int

@dataclass
class PublishFirmwareResponsePayload:
    status: str

@dataclass
class PublishFirmwareStatusNotificationRequestPayload:
    status: str

@dataclass
class ReportChargingProfilesRequestPayload:
    requestId: int
    chargingLimitSource: str
    evseId: int
    chargingProfile: Dict

@dataclass 
class RequestStartTransactionResponsePayload:
    status: str

@dataclass
class RequestStopTransactionResponsePayload:
    status: str

@dataclass
class ReservationStatusUpdateRequestPayload:
    reservationId: int
    reservationUpdateStatus: str

@dataclass
class ReserveNowResponsePayload:
    status: str

@dataclass
class ResetResponsePayload:
    status: str

@dataclass
class SecurityEventNotificationRequestPayload:
    type: str
    timestamp: str

@dataclass
class SendLocalListResponsePayload:
    status: str

@dataclass
class SetChargingProfileResponsePayload:
    status: str

@dataclass
class SetDisplayMessageResponsePayload:
    status: str

@dataclass
class SetMonitoringBaseResponsePayload:
    status: str

@dataclass
class SetMonitoringLevelResponsePayload:
    status: str

@dataclass
class SetNetworkProfileResponsePayload:
    status: str

@dataclass
class SetVariableMonitoringResponsePayload:
    setMonitoringResult: Dict

@dataclass
class SetVariablesResponsePayload:
    setVariableResult: Dict

@dataclass
class SignCertificateRequestPayload:
    csr: str

@dataclass
class StatusNotificationRequestPayload:
    timestamp: str
    connectorStatus: str
    evseId: int
    connectorId: int

@dataclass
class TransactionEventRequestPayload:
    eventType: str
    timestamp: str
    triggerReason: str
    seqNo: int
    transactionInfo: Dict

@dataclass
class TriggerMessageResponsePayload:
    status: str

@dataclass
class UnlockConnectorResponsePayload:
    status: str

@dataclass
class UnpublishFirmwareResponsePayload:
    status: str
    
@dataclass
class UpdateFirmwareResponsePayload:
    status: str























    









