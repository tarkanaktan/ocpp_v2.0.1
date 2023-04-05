
class ConnectorStatusEnumType():
    Available = "Available"
    Occupied = "Occupied"
    Reserved = "Reserved"
    Unavailable = "Unavailable"
    Faulted = "Faulted"
    Uninitialized = ""

    attrlist = ["Available","Occupied","Reserved","Unavailable","Faulted"]

class RegistrationStatusEnumType():
    Accepted = "Accepted"
    Pending = "Pending"
    Rejected = "Rejected"

class APNAuthenticationEnumType():
    CHAP = "CHAP"
    NONE = "NONE"
    PAP = "PAP"
    AUTO = "AUTO"

class AttributeEnumType():
    Actual = "Actual"
    Target = "Target"
    MinSet = "MinSet"
    MaxSet = "MaxSet"

class AuthorizationStatusEnumType():
    Accepted = "Accepted"
    Blocked = "Blocked"
    ConcurrentTx = "ConcurrentTx"
    Expired = "Expired"
    Invalid = "Invalid"
    NoCredit = "NoCredit"
    NotAllowedTypeEVSE = "NotAllowedTypeEVSE"
    NotAtThisLocation ="NotAtThisLocation"
    NotAtThisTime ="NotAtThisTime"
    Unknown ="Unknown"

class AuthorizeCertificateStatusEnumType():
    Accepted = "Accepted"
    SignatureError = "SignatureError"
    CertificateExpired = "CertificateExpired"
    CertificateRevoked = "CertificateRevoked"
    NoCertificateAvailable = "NoCertificateAvailable"
    CertChainError = "CertChainError"
    ContractCancelled = "ContractCancelled"

class BootReasonEnumType:
    ApplicationReset = "ApplicationReset"
    FirmwareUpdate = "FirmwareUpdate"
    LocalReset = "LocalReset"
    PowerUp = "PowerUp"
    RemoteReset = "RemoteReset"
    ScheduledReset = "ScheduledReset"
    Triggered = "Triggered"
    Unknown = "Unknown"
    Watchdog = "Watchdog"

class CancelReservationStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"

class CertificateActionEnumType():
    Install = "Install"
    Update = "Update"

class CertificateSignedStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"

class CertificateSigningUseEnumType():
    ChargingStationCertificate = "ChargingStationCertificate"
    V2GCertificate = "V2GCertificate"

class ChangeAvailabilityStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Scheduled = "Scheduled"

class ChargingLimitSourceEnumType():
    EMS = "EMS"
    Other ="Other"
    SO = "SO"
    CSO = "CSO"

class ChargingProfileKindEnumType():
    Absolute = "Absolute"
    Recurring = "Recurring"
    Relative = "Relative"

class ChargingProfilePurposeEnumType():
    ChargingStationExternalConstraints = "ChargingStationExternalConstraints"
    ChargingStationMaxProfile = "ChargingStationMaxProfile"
    TxDefaultProfile = "TxDefaultProfile"
    TxProfile = "TxProfile"

class ChargingProfileStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"

class ChargingRateUnitEnumType():
    W = "W"
    A = "A"

class ChargingStateEnumType():
    Charging = "Charging"
    EVConnected = "EVConnected"
    SuspendedEV = "SuspendedEV"
    SuspendedEVSE = "SuspendedEVSE"
    Idle = "Idle"  

class ClearCacheStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"

class ClearChargingProfileStatusEnumType():
    Accepted = "Accepted"
    Unknown = "Unknown"

class ClearMessageStatusEnumType():
    Accepted = "Accepted"
    Unknown = "Unknown"

class ClearMonitoringStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    NotFound = "NotFound"

class ComponentCriterionEnumType():
    Active = "Active"
    Available = "Available"
    Enabled = "Enabled"
    Problem = "Problem"

class ConnectorEnumType():
    cCCS1 = "cCCS1"
    cCCS2 = "cCCS2"
    cG105 = "cG105"
    cTesla = "cTesla"
    cType1 = "cType1"
    cType2 = "cType2"
    s309_1P_16A = "s309-1P-16A"
    s309_1P_32A = "s309-1P-32A"
    s309_3P_16A = "s309-3P-16A"
    s309_3P_32A = "s309-3P-32A"
    sBS1361 = "sBS1361"
    sCEE_7_7 = "sCEE-7-7"
    sType2 = "sType2"
    sType3 = "sType3"
    Other1PhMax16A = "Other1PhMax16A"
    Other1PhOver16A ="Other1PhOver16A"
    Other3Ph = "Other3Ph"
    Pan = "Pan"
    wInductive = "wInductive"
    wResonant = "wResonant"
    Undetermined = "Undetermined"
    Unknown = "Unknown"

class CostKindEnumType():
    CarbonDioxideEmission = "CarbonDioxideEmission"
    RelativePricePercentage = "RelativePricePercentage"
    RenewableGenerationPercentage = "RenewableGenerationPercentage"

class CustomerInformationStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Invalid = "Invalid"

class DataEnumType():
    string = "string"
    decimal = "decimal"
    integer = "integer"
    dateTime = "dateTime"
    boolean = "boolean"
    OptionList = "OptionList"
    SequenceList = "SequenceList"
    MemberList = "MemberList"
    
class DeleteCertificateStatusEnumType():
    Accepted = "Accepted"
    Failed = "Failed"
    NotFound = "NotFound"

class DataTransferStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    UnknownMessageId = "UnknownMessageId"
    UnknownVendorId = "UnknownVendorId"

class DisplayMessageStatusEnumType():
    Accepted = "Accepted"
    NotSupportedMessageFormat = "NotSupportedMessageFormat"
    Rejected = "Rejected"
    NotSupportedPriority = "NotSupportedPriority"
    NotSupportedState = "NotSupportedState"
    UnknownTransaction = "UnknownTransaction"

class EnergyTransferModeEnumType():
    DC = "DC"
    AC_single_phase = "AC_single_phase"
    AC_two_phase = "AC_two_phase"
    AC_three_phase = "AC_three_phase"

class EventNotificationEnumType():
    HardWiredNotification = "HardWiredNotification"
    HardWiredMonitor = "HardWiredMonitor"
    PreconfiguredMonitor = "PreconfiguredMonitor"
    CustomMonitor = "CustomMonitor"

class EventTriggerEnumType():
    Alerting = "Alerting"
    Delta = "Delta"
    Periodic = "Periodic"

class FirmwareStatusEnumType():
    Downloaded = "Downloaded"
    DownloadFailed = "DownloadFailed"
    Downloading = "Downloading"
    DownloadScheduled = "DownloadScheduled"
    DownloadPaused = "DownloadPaused"
    Idle = "Idle"
    InstallationFailed = "InstallationFailed"
    Installing = "Installing"
    Installed = "Installed"
    InstallRebooting = "InstallRebooting"
    InstallScheduled = "InstallScheduled"
    InstallVerificationFailed = "InstallVerificationFailed"
    InvalidSignature = "InvalidSignature"
    SignatureVerified = "SignatureVerified"  

class GenericDeviceModelStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    NotSupported = "NotSupported"
    EmptyResultSet = "EmptyResultSet"

class GenericStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"

class GetCertificateIdUseEnumType():
    V2GRootCertificate = "V2GRootCertificate"
    MORootCertificate = "MORootCertificate"
    CSMSRootCertificate = "CSMSRootCertificate"
    V2GCertificateChain = "V2GCertificateChain"
    ManufacturerRootCertificate = "ManufacturerRootCertificate"

class GetCertificateStatusEnumType():
    Accepted = "Accepted"
    Failed = "Failed"

class GetChargingProfileStatusEnumType():
    Accepted = "Accepted"
    NoProfiles = "NoProfiles"

class GetDisplayMessagesStatusEnumType():
    Accepted = "Accepted"
    Unknown = "Unknown"

class GetInstalledCertificateStatusEnumType():
    Accepted = "Accepted"
    NotFound = "NotFound"

class GetVariableStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    UnknownComponent = "UnknownComponent"
    UnknownVariable = "UnknownVariable"
    NotSupportedAttributeType = "NotSupportedAttributeType"

class HashAlgorithmEnumType():
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"

class IdTokenEnumType():
    Central = "Central"
    eMAID = "eMAID"
    ISO14443 = "ISO14443"
    ISO15693 = "ISO15693"
    KeyCode = "KeyCode"
    Local = "Local"
    MacAddress = "MacAddress"
    NoAuthorization = "NoAuthorization"

class InstallCertificateStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Failed = "Failed"

class InstallCertificateUseEnumType():
    V2GRootCertificate = "V2GRootCertificate"
    MORootCertificate = "MORootCertificate"
    CSMSRootCertificate = "CSMSRootCertificate"
    ManufacturerRootCertificate = "ManufacturerRootCertificate"

class Iso15118EVCertificateStatusEnumType():
    Accepted = "Accepted"
    Failed = "Failed"

class LocationEnumType():
    Body = "Body"
    Cable = "Cable"
    EV = "EV"
    Inlet = "Inlet"
    Outlet = "Outlet"

class LogEnumType():
    DiagnosticsLog = "DiagnosticsLog"
    SecurityLog = "SecurityLog"

class LogStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    AcceptedCanceled = "AcceptedCanceled"

class MeasurandEnumType():
    Current_Export = "Current.Export"
    Current_Import = "Current.Import" 
    Current_Offered = "Current.Offered"
    Energy_Active_Export_Register = "Energy.Active.Export.Register"
    Energy_Active_Import_Register = "Energy.Active.Import.Register"
    Energy_Reactive_Export_Register = "Energy.Reactive.Export.Register"
    Energy_Reactive_Import_Register = "Energy.Reactive.Import.Register"
    Energy_Active_Export_Interval = "Energy.Active.Export.Interval"
    Energy_Active_Import_Interval = "Energy.Active.Import.Interval"
    Energy_Reactive_Export_Interval = "Energy.Reactive.Export.Interval"
    Energy_Reactive_Import_Interval = "Energy.Reactive.Import.Interval"
    Energy_Active_Net = "Energy.Active.Net"
    Energy_Reactive_Net = "Energy.Reactive.Net"
    Energy_Apparent_Net = "Energy.Apparent.Net"
    Energy_Apparent_Import = "Energy.Apparent.Import"
    Energy_Apparent_Export = "Energy.Apparent.Export"
    Frequency = "Frequency"
    Power_Active_Export = "Power.Active.Export"
    Power_Active_Import = "Power.Active.Import"
    Power_Reactive_Export = "Power.Reactive.Export"
    Power_Reactive_Import = "Power.Reactive.Import"
    Power_Factor = "Power.Factor"
    Power_Offered = "Power.Offered"
    SoC = "SoC"
    Voltage = "Voltage"

class MessageFormatEnumType():
    ASCII = "ASCII"
    HTML = "HTML"
    URI = "URI"    
    UTF8 = "UTF8"

class MessagePriorityEnumType():
    AlwaysFront = "AlwaysFront"
    InFront = "InFront"
    NormalCycle = "NormalCycle"

class MessageStateEnumType():
    Charging = "Charging"
    Idle = "Idle"
    Unavailable = "Unavailable"
    Faulted = "Faulted"

class MessageTriggerEnumType():
    BootNotification = "BootNotification"
    LogStatusNotification = "LogStatusNotification"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    Heartbeat = "Heartbeat"
    MeterValues = "MeterValues"
    SignChargingStationCertificate = "SignChargingStationCertificate"
    SignV2GCertificate = "SignV2GCertificate"
    StatusNotification = "StatusNotification"
    TransactionEvent = "TransactionEvent"
    SignCombinedCertificate = "SignCombinedCertificate"
    PublishFirmwareStatusNotification = "PublishFirmwareStatusNotification"

class MonitorEnumType():
    UpperThreshold = "UpperThreshold"
    LowerThreshold = "LowerThreshold"
    Delta = "Delta"
    Periodic = "Periodic"
    PeriodicClockAligned = "PeriodicClockAligned"

class MonitoringBaseEnumType():
    All = "All"
    FactoryDefault = "FactoryDefault"
    HardWiredOnly = "HardWiredOnly"

class MonitoringCriterionEnumType():
    ThresholdMonitoring = "ThresholdMonitoring"
    DeltaMonitoring = "DeltaMonitoring"
    PeriodicMonitoring = "PeriodicMonitoring"

class MutabilityEnumType():
    ReadOnly = "ReadOnly"
    WriteOnly = "WriteOnly"
    ReadWrite = "ReadWrite"
    
class NotifyEVChargingNeedsStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Processing = "Processing"

class OCPPInterfaceEnumType():
    Wired0 = "Wired0"
    Wired1 = "Wired1"
    Wired2 = "Wired2"
    Wired3 = "Wired3"
    Wireless0 = "Wireless0"
    Wireless1 = "Wireless1"
    Wireless2 = "Wireless2"
    Wireless3 = "Wireless3"

class OCPPTransportEnumType():
    JSON = "JSON"
    SOAP = "SOAP"

class OCPPVersionEnumType():
    OCPP12 = "OCPP12"
    OCPP15 = "OCPP15"
    OCPP16 = "OCPP16"
    OCPP20 = "OCPP20"

class OperationalStatusEnumType():
    Operative = "Operative"
    Inoperative = "Inoperative"
    
class PhaseEnumType():
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    N = "N"
    L1_N = "L1-N"
    L2_N = "L2-N"
    L3_N = "L3-N"
    L1_L2 = "L1-L2"
    L2_L3 = "L2-L3"
    L3_L1 = "L3-L1"

class PublishFirmwareStatusEnumType():
    Downloaded = "Downloaded"
    DownloadFailed = "DownloadFailed"
    Downloading = "Downloading"
    DownloadScheduled = "DownloadScheduled"
    DownloadPaused = "DownloadPaused"
    Idle = "Idle"
    Published = "Published"
    InvalidChecksum = "InvalidChecksum"
    ChecksumVerified = "ChecksumVerified"
    PublishFailed = "PublishFailed"
    
class ReadingContextEnumType():
    Interruption_Begin = "Interruption.Begin"
    Interruption_End = "Interruption.End"
    Other = "Other"
    Sample_Clock = "Sample.Clock"
    Sample_Periodic = "Sample.Periodic"
    Transaction_Begin = "Transaction.Begin"
    Transaction_End = "Transaction.End"
    Trigger = "Trigger"

class ReasonEnumType():
    DeAuthorized = "DeAuthorized"
    EmergencyStop = "EmergencyStop"
    EnergyLimitReached = "EnergyLimitReached"
    EVDisconnected = "EVDisconnected"
    GroundFault = "GroundFault"
    ImmediateReset = "ImmediateReset"
    Local = "Local"
    LocalOutOfCredit = "LocalOutOfCredit"
    MasterPass = "MasterPass"
    Other = "Other"
    OvercurrentFault = "OvercurrentFault"
    PowerLoss = "PowerLoss"
    PowerQuality = "PowerQuality"
    Reboot = "Reboot"
    Remote = "Remote"
    SOCLimitReached = "SOCLimitReached"
    StoppedByEV = "StoppedByEV"
    TimeLimitReached = "TimeLimitReached"
    Timeout = "Timeout"

class RecurrencyKindEnumType():
    Daily = "Daily"
    Weekly = "Weekly"

class ReportBaseEnumType():
    ConfigurationInventory = "ConfigurationInventory"
    FullInventory = "FullInventory"
    SummaryInventory = "SummaryInventory"

class RequestStartStopStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"

class ReservationUpdateStatusEnumType():
    Expired = "Expired"
    Removed = "Removed"

class ReserveNowStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Occupied = "Occupied"
    Unavailable = "Unavailable"
    Faulted = "Faulted"

class ResetEnumType():
    Immediate = "Immediate"
    OnIdle = "OnIdle"

class ResetStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Scheduled = "Scheduled"

class SendLocalListStatusEnumType():
    Accepted = "Accepted"
    Failed = "Failed"
    VersionMismatch = "VersionMismatch"

class SetMonitoringStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    UnknownComponent = "UnknownComponent"
    UnknownVariable = "UnknownVariable"
    UnsupportedMonitorType = "UnsupportedMonitorType"
    Duplicate = "Duplicate"
    
class SetNetworkProfileStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    Failed = "Failed"
    
class SetVariableStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    UnknownComponent = "UnknownComponent"
    UnknownVariable = "UnknownVariable"
    NotSupportedAttributeType = "NotSupportedAttributeType"
    RebootRequired = "RebootRequired"

class TransactionEventEnumType():
    Ended = "Ended"
    Started = "Started"
    Updated = "Updated"

class TriggerMessageStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    NotImplemented = "NotImplemented"

class TriggerReasonEnumType():
    Authorized = "Authorized"
    CablePluggedIn = "CablePluggedIn"
    ChargingRateChanged = "ChargingRateChanged"
    ChargingStateChanged = "ChargingStateChanged"
    Deauthorized = "Deauthorized"
    EnergyLimitReached = "EnergyLimitReached"
    EVCommunicationLost = "EVCommunicationLost"
    EVConnectTimeout = "EVConnectTimeout"
    MeterValueClock = "MeterValueClock"
    MeterValuePeriodic = "MeterValuePeriodic"
    TimeLimitReached = "TimeLimitReached"
    Trigger = "Trigger"
    UnlockCommand = "UnlockCommand"
    StopAuthorized = "StopAuthorized"
    EVDeparted = "EVDeparted"
    EVDetected = "EVDetected"
    RemoteStop = "RemoteStop"
    RemoteStart = "RemoteStart"
    AbnormalCondition = "AbnormalCondition"
    SignedDataReceived = "SignedDataReceived"
    ResetCommand = "ResetCommand"

class UnlockStatusEnumType():
    Unlocked = "Unlocked"
    UnlockFailed = "UnlockFailed"
    OngoingAuthorizedTransaction = "OngoingAuthorizedTransaction"
    UnknownConnector = "UnknownConnector"

class UnpublishFirmwareStatusEnumType():
    DownloadOngoing = "DownloadOngoing"
    NoFirmware = "NoFirmware"
    Unpublished = "Unpublished"
    
class UpdateEnumType():
    Differential = "Differential"
    Full = "Full"

class UpdateFirmwareStatusEnumType():
    Accepted = "Accepted"
    Rejected = "Rejected"
    AcceptedCanceled = "AcceptedCanceled"
    InvalidCertificate = "InvalidCertificate"
    RevokedCertificate = "RevokedCertificate"

class UploadLogStatusEnumType():
    BadMessage = "BadMessage"
    Idle = "Idle" 
    NotSupportedOperation = "NotSupportedOperation"
    PermissionDenied = "PermissionDenied"
    Uploaded = "Uploaded"
    UploadFailure = "UploadFailure"
    Uploading = "Uploading"
    AcceptedCanceled = "AcceptedCanceled"

class VPNEnumType():
    IKEv2 = "IKEv2"
    IPSec = "IPSec"
    L2TP = "L2TP"
    PPTP = "PPTP"
    




















