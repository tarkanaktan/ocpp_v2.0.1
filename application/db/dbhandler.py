import sqlite3
import asyncio
#from application.db.variables import *

class dbValueEnums():
    #ret contains id,ocppName,componentName,variableName,variableInstance,dataType,mutability,value
    id = 0
    ocppName = 1
    componentName = 2
    variableName = 3
    variableInstance = 4
    dataType = 5
    mutability = 6
    value = 7


defaultVariables = [
    #General
    {"ocppName": "ActiveNetworkProfile","componentName": "OCPPCommCtrlr","variableName":"ActiveNetworkProfile","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value":1},
    {"ocppName": "AllowNewSessionsPendingFirmwareUpdate","componentName": "ChargingStation","variableName":"AllowNewSessionsPendingFirmwareUpdate","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "DefaultMessageTimeout","componentName": "OCPPCommCtrlr","variableName":"MessageTimeout","variableInstance":"Default","dataType":"int","mutability": "ReadOnly", "value": 30},
    {"ocppName": "FileTransferProtocols","componentName": "OCPPCommCtrlr","variableName":"FileTransferProtocols","variableInstance":None,"dataType":"MemberList","mutability": "ReadOnly", "value": set(("FTP","FTPS"))},
    {"ocppName": "HeartbeatInterval","componentName": "OCPPCommCtrlr","variableName":"HeartbeatInterval","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 60},
    {"ocppName": "NetworkConfigurationPriority","componentName": "OCPPCommCtrlr","variableName":"NetworkConfigurationPriority","variableInstance":None,"dataType":"SequenceList","mutability": "ReadWrite", "value": set(("",))},
    {"ocppName": "NetworkProfileConnectionAttempts","componentName": "OCPPCommCtrlr","variableName":"NetworkProfileConnectionAttempts","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 10},
    {"ocppName": "OfflineThreshold","componentName": "OCPPCommCtrlr","variableName":"OfflineThreshold","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 30},
    {"ocppName": "QueueAllMessages","componentName": "OCPPCommCtrlr","variableName":"QueueAllMessages","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "MessageAttemptsTransactionEvent","componentName": "OCPPCommCtrlr","variableName":"MessageAttempts","variableInstance":"TransactionEvent","dataType":"int","mutability": "ReadWrite", "value": 3},
    {"ocppName": "MessageAttemptIntervalTransactionEvent","componentName": "OCPPCommCtrlr","variableName":"MessageAttemptInterval","variableInstance":"TransactionEvent","dataType":"int","mutability": "ReadWrite", "value": 60},
    {"ocppName": "UnlockOnEVSideDisconnect","componentName": "OCPPCommCtrlr","variableName":"UnlockOnEVSideDisconnect","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "WebSocketPingInterval","componentName": "OCPPCommCtrlr","variableName":"WebSocketPingInterval","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 5},
    {"ocppName": "ResetRetries","componentName": "OCPPCommCtrlr","variableName":"ResetRetries","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 3},
    {"ocppName": "MessageFieldLength","componentName": "OCPPCommCtrlr","variableName":"FieldLength","variableInstance":"<message>.<field>","dataType":"int","mutability": "ReadOnly", "value": 100}, #check field length
    {"ocppName": "ItemsPerMessageGetReport","componentName": "DeviceDataCtrlr","variableName":"ItemsPerMessage","variableInstance":"GetReport","dataType":"int","mutability": "ReadOnly", "value": 9999},
    {"ocppName": "ItemsPerMessageGetVariables","componentName": "DeviceDataCtrlr","variableName":"ItemsPerMessage","variableInstance":"GetVariables","dataType":"int","mutability": "ReadOnly", "value": 9999},
    {"ocppName": "BytesPerMessageGetReport","componentName": "DeviceDataCtrlr","variableName":"BytesPerMessage","variableInstance":"GetReport","dataType":"int","mutability": "ReadOnly", "value": 9999},
    {"ocppName": "BytesPerMessageGetVariables","componentName": "DeviceDataCtrlr","variableName":"BytesPerMessage","variableInstance":"GetVariables","dataType":"int","mutability": "ReadOnly", "value": 9999},
    {"ocppName": "ConfigurationValueSize","componentName": "DeviceDataCtrlr","variableName":"ConfigurationValueSize","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 1000},
    {"ocppName": "ReportingValueSize","componentName": "DeviceDataCtrlr","variableName":"ReportingValueSize","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 2500},
    {"ocppName": "ItemsPerMessageSetVariables","componentName": "DeviceDataCtrlr","variableName":"ItemsPerMessage","variableInstance":"SetVariables","dataType":"int","mutability": "ReadOnly", "value": 9999},
    {"ocppName": "BytesPerMessageSetVariables","componentName": "DeviceDataCtrlr","variableName":"BytesPerMessage","variableInstance":"SetVariables","dataType":"int","mutability": "ReadOnly", "value": 9999},
    {"ocppName": "DateTime","componentName": "ClockCtrlr","variableName":"DateTime","variableInstance":None,"dataType":"DateTime","mutability": "ReadOnly", "value": "2023-01-01T00:00:00"},
    {"ocppName": "NtpSource","componentName": "ClockCtrlr","variableName":"NtpSource","variableInstance":None,"dataType":"OptionList","mutability": "ReadWrite", "value":"DHCP"},
    {"ocppName": "NtpServerUri","componentName": "ClockCtrlr","variableName":"NtpServerUri","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": ""}, #check instance
    {"ocppName": "TimeOffset","componentName": "ClockCtrlr","variableName":"TimeOffset","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "+02:00"},
    {"ocppName": "NextTimeOffsetTransitionDateTime","componentName": "ClockCtrlr","variableName":"NextTimeOffsetTransitionDateTime","variableInstance":None,"dataType":"DateTime","mutability": "ReadWrite", "value": ""},
    {"ocppName": "TimeOffsetNextTransition","componentName": "ClockCtrlr","variableName":"TimeOffset","variableInstance":"NextTransition","dataType":"str","mutability": "ReadWrite", "value": "+00:00"},
    {"ocppName": "TimeSource","componentName": "ClockCtrlr","variableName":"TimeSource","variableInstance":None,"dataType":"SequenceList","mutability": "ReadWrite", "value": set(("Heartbeat","NTP"))},
    {"ocppName": "TimeZone","componentName": "ClockCtrlr","variableName":"TimeZone","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "Europe/Ist"},
    {"ocppName": "TimeAdjustmentReportingThreshold","componentName": "ClockCtrlr","variableName":"TimeAdjustmentReportingThreshold","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 20},
    {"ocppName": "CustomImplementationEnabled","componentName": "CustomizationCtrlr","variableName":"CustomImplementationEnabled","variableInstance":"<VendorId>","dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Security
    {"ocppName": "BasicAuthPassword","componentName": "SecurityCtrlr","variableName":"BasicAuthPassword","variableInstance":None,"dataType":"passwordString","mutability": "WriteOnly", "value": ""}, #TODO create dataType
    {"ocppName": "Identity","componentName": "SecurityCtrlr","variableName":"Identity","variableInstance":None,"dataType":"identifierString","mutability": "ReadWrite", "value": ""}, #TODO create dataType
    {"ocppName": "OrganizationName","componentName": "SecurityCtrlr","variableName":"OrganizationName","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": ""},
    {"ocppName": "CertificateEntries","componentName": "SecurityCtrlr","variableName":"CertificateEntries","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 5},
    {"ocppName": "SecurityProfile","componentName": "SecurityCtrlr","variableName":"SecurityProfile","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 0},
    {"ocppName": "AdditionalRootCertificateCheck","componentName": "SecurityCtrlr","variableName":"AdditionalRootCertificateCheck","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "MaxCertificateChainSize","componentName": "SecurityCtrlr","variableName":"MaxCertificateChainSize","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 10000},
    {"ocppName": "CertSigningWaitMinimum","componentName": "SecurityCtrlr","variableName":"CertSigningWaitMinimum","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 120},
    {"ocppName": "CertSigningRepeatTimes","componentName": "SecurityCtrlr","variableName":"CertSigningRepeatTimes","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 5},
    #Authorization related
    {"ocppName": "AuthEnabled","componentName": "AuthCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "AdditionalInfoItemsPerMessage","componentName": "AuthCtrlr","variableName":"AdditionalInfoItemsPerMessage","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 0},
    {"ocppName": "OfflineTxForUnknownIdEnabled","componentName": "AuthCtrlr","variableName":"OfflineTxForUnknownIdEnabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "AuthorizeRemoteStart","componentName": "AuthCtrlr","variableName":"AuthorizeRemoteStart","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "LocalAuthorizeOffline","componentName": "AuthCtrlr","variableName":"LocalAuthorizeOffline","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "LocalPreAuthorize","componentName": "AuthCtrlr","variableName":"LocalPreAuthorize","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "MasterPassGroupId","componentName": "AuthCtrlr","variableName":"MasterPassGroupId","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": ""},
    {"ocppName": "DisableRemoteAuthorization","componentName": "AuthCtrlr","variableName":"DisableRemoteAuthorization","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Authorization Cache related
    {"ocppName": "AuthCacheEnabled","componentName": "AuthCacheCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "AuthCacheAvailable","componentName": "AuthCacheCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "AuthCacheLifeTime","componentName": "AuthCacheCtrlr","variableName":"LifeTime","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 2592000}, #one month
    {"ocppName": "AuthCacheStorage","componentName": "AuthCacheCtrlr","variableName":"Storage","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 10000},
    {"ocppName": "AuthCachePolicy","componentName": "AuthCacheCtrlr","variableName":"Policy","variableInstance":None,"dataType":"OptionList","mutability": "ReadWrite", "value": "CUSTOM"},
    {"ocppName": "AuthCacheDisablePostAuthorize","componentName": "AuthCacheCtrlr","variableName":"DisablePostAuthorize","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Local Authorization List Management related
    {"ocppName": "LocalAuthListEnabled","componentName": "LocalAuthListCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "LocalAuthListEntries","componentName": "LocalAuthListCtrlr","variableName":"Entries","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 10000},
    {"ocppName": "LocalAuthListAvailable","componentName": "LocalAuthListCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "ItemsPerMessageSendLocalList","componentName": "LocalAuthListCtrlr","variableName":"ItemsPerMessage","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 10000},
    {"ocppName": "BytesPerMessageSendLocalList","componentName": "LocalAuthListCtrlr","variableName":"BytesPerMessage","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 14},
    {"ocppName": "LocalAuthListStorage","componentName": "LocalAuthListCtrlr","variableName":"Storage","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 140000},
    {"ocppName": "LocalAuthListDisablePostAuthorize","componentName": "LocalAuthListCtrlr","variableName":"DisablePostAuthorize","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Transaction related
    {"ocppName": "EVConnectionTimeOut","componentName": "TxCtrlr","variableName":"EVConnectionTimeOut","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 30},
    {"ocppName": "StopTxOnEVSideDisconnect","componentName": "TxCtrlr","variableName":"StopTxOnEVSideDisconnect","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "TxBeforeAcceptedEnabled","componentName": "TxCtrlr","variableName":"TxBeforeAcceptedEnabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "TxStartPoint","componentName": "TxCtrlr","variableName":"TxStartPoint","variableInstance":None,"dataType":"MemberList","mutability": "ReadOnly", "value": set(("EVConnected","Authorized"))},
    {"ocppName": "TxStopPoint","componentName": "TxCtrlr","variableName":"TxStopPoint","variableInstance":None,"dataType":"MemberList","mutability": "ReadOnly", "value": set(("EVConnected","Authorized"))},
    {"ocppName": "MaxEnergyOnInvalidId","componentName": "TxCtrlr","variableName":"MaxEnergyOnInvalidId","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 30},
    {"ocppName": "StopTxOnInvalidId","componentName": "TxCtrlr","variableName":"StopTxOnInvalidId","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Metering related
    {"ocppName": "SampledDataEnabled","componentName": "SampledDataCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "SampledDataAvailable","componentName": "SampledDataCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "SampledDataSignReadings","componentName": "SampledDataCtrlr","variableName":"SignReadings","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "SampledDataTxEndedMeasurands","componentName": "SampledDataCtrlr","variableName":"TxEndedMeasurands","variableInstance":None,"dataType":"MemberList","mutability": "ReadWrite", "value": "Energy.Active.Import.Register"},
    {"ocppName": "SampledDataTxEndedInterval","componentName": "SampledDataCtrlr","variableName":"TxEndedInterval","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 60},
    {"ocppName": "SampledDataTxStartedMeasurands","componentName": "SampledDataCtrlr","variableName":"TxStartedMeasurands","variableInstance":None,"dataType":"MemberList","mutability": "ReadWrite", "value": "Energy.Active.Import.Register"},
    {"ocppName": "SampledDataTxUpdatedMeasurands","componentName": "SampledDataCtrlr","variableName":"TxUpdatedMeasurands","variableInstance":None,"dataType":"MemberList","mutability": "ReadWrite", "value": "Energy.Active.Import.Register"},
    {"ocppName": "SampledDataTxUpdatedInterval","componentName": "SampledDataCtrlr","variableName":"TxUpdatedInterval","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 60},
    {"ocppName": "AlignedDataEnabled","componentName": "AlignedDataCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "AlignedDataAvailable","componentName": "AlignedDataCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "AlignedDataMeasurands","componentName": "AlignedDataCtrlr","variableName":"Measurands","variableInstance":None,"dataType":"MemberList","mutability": "ReadWrite", "value": "Energy.Active.Import.Register"},
    {"ocppName": "AlignedDataInterval","componentName": "AlignedDataCtrlr","variableName":"Interval","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 60},
    {"ocppName": "AlignedDataSendDuringIdle","componentName": "AlignedDataCtrlr","variableName":"SendDuringIdle","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "AlignedDataSignReadings","componentName": "AlignedDataCtrlr","variableName":"SignReadings","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "AlignedDataTxEndedMeasurands","componentName": "AlignedDataCtrlr","variableName":"TxEndedMeasurands","variableInstance":None,"dataType":"MemberList","mutability": "ReadWrite", "value": "Energy.Active.Import.Register"},
    {"ocppName": "AlignedDataTxEndedInterval","componentName": "AlignedDataCtrlr","variableName":"TxEndedInterval","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 60},
    {"ocppName": "PublicKeyWithSignedMeterValue","componentName": "OCPPCommCtrlr","variableName":"PublicKeyWithSignedMeterValue","variableInstance":None,"dataType":"OptionList","mutability": "ReadWrite", "value": "Never"},
    {"ocppName": "SampledDataRegisterValuesWithoutPhases","componentName": "SampledDataCtrlr","variableName":"RegisterValuesWithoutPhases","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Reservation related
    {"ocppName": "ReservationEnabled","componentName": "ReservationCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ReservationAvailable","componentName": "ReservationCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "ReservationNonEvseSpecific","componentName": "ReservationCtrlr","variableName":"NonEvseSpecific","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    #Smart Charging related
    {"ocppName": "SmartChargingEnabled","componentName": "SmartChargingCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "SmartChargingAvailable","componentName": "SmartChargingCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "ACPhaseSwitchingSupported","componentName": "SmartChargingCtrlr","variableName":"ACPhaseSwitchingSupported","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "ChargingProfileMaxStackLevel","componentName": "SmartChargingCtrlr","variableName":"ProfileStackLevel","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 5},
    {"ocppName": "ChargingScheduleChargingRateUnit","componentName": "SmartChargingCtrlr","variableName":"RateUnit","variableInstance":None,"dataType":"MemberList","mutability": "ReadOnly", "value": set(("A","W"))},
    {"ocppName": "PeriodsPerSchedule","componentName": "SmartChargingCtrlr","variableName":"PeriodsPerSchedule","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 5},
    {"ocppName": "ExternalControlSignalsEnabled","componentName": "SmartChargingCtrlr","variableName":"ExternalControlSignalsEnabled","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "NotifyChargingLimitWithSchedules","componentName": "SmartChargingCtrlr","variableName":"NotifyChargingLimitWithSchedules","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "Phases3to1","componentName": "SmartChargingCtrlr","variableName":"Phases3to1","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "ChargingProfileEntries","componentName": "SmartChargingCtrlr","variableName":"Entries","variableInstance":"ChargingProfiles","dataType":"int","mutability": "ReadOnly", "value": 5},
    {"ocppName": "LimitChangeSignificance","componentName": "SmartChargingCtrlr","variableName":"LimitChangeSignificance","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 5},
    #Tariff & Cost related
    {"ocppName": "TariffEnabled","componentName": "TariffCostCtrlr","variableName":"Enabled","variableInstance":"Tariff","dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "TariffAvailable","componentName": "TariffCostCtrlr","variableName":"Available","variableInstance":"Tariff","dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "TariffFallbackMessage","componentName": "TariffCostCtrlr","variableName":"TariffFallbackMessage","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "There is no driver specific tariff information available"},
    {"ocppName": "CostEnabled","componentName": "TariffCostCtrlr","variableName":"Enabled","variableInstance":"Cost","dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "CostAvailable","componentName": "TariffCostCtrlr","variableName":"Available","variableInstance":"Cost","dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "TotalCostFallbackMessage","componentName": "TariffCostCtrlr","variableName":"TotalCostFallbackMessage","variableInstance":"Tariff","dataType":"str","mutability": "ReadWrite", "value": "Cannot retrieve the cost for a transaction"},
    {"ocppName": "Currency","componentName": "TariffCostCtrlr","variableName":"Currency","variableInstance":"Tariff","dataType":"str","mutability": "ReadWrite", "value": "EUR"},
    #Diagnostics related
    {"ocppName": "MonitoringEnabled","componentName": "MonitoringCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "MonitoringAvailable","componentName": "MonitoringCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "ItemsPerMessageClearVariableMonitoring","componentName": "MonitoringCtrlr","variableName":"ItemsPerMessage","variableInstance":"ClearVariableMonitoring","dataType":"int","mutability": "ReadOnly", "value": 5},
    {"ocppName": "ItemsPerMessageSetVariableMonitoring","componentName": "MonitoringCtrlr","variableName":"ItemsPerMessage","variableInstance":"SetVariableMonitoring","dataType":"int","mutability": "ReadOnly", "value": 5},
    {"ocppName": "BytesPerMessageClearVariableMonitoring","componentName": "MonitoringCtrlr","variableName":"BytesPerMessage","variableInstance":"ClearVariableMonitoring","dataType":"int","mutability": "ReadOnly", "value": 10000},
    {"ocppName": "BytesPerMessageSetVariableMonitoring","componentName": "MonitoringCtrlr","variableName":"BytesPerMessage","variableInstance":"SetVariableMonitoring","dataType":"int","mutability": "ReadOnly", "value": 10000},
    {"ocppName": "OfflineMonitoringEventQueuingSeverity","componentName": "MonitoringCtrlr","variableName":"OfflineQueuingSeverity","variableInstance":None,"dataType":"int","mutability": "ReadWrite", "value": 0},
    {"ocppName": "ActiveMonitoringBase","componentName": "MonitoringCtrlr","variableName":"ActiveMonitoringBase","variableInstance":None,"dataType":"OptionList","mutability": "ReadOnly", "value": set(("All","FactoryDefault","HardwiredOnly"))},
    {"ocppName": "ActiveMonitoringLevel","componentName": "MonitoringCtrlr","variableName":"ActiveMonitoringLevel","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 0},
    #Display Message related
    {"ocppName": "DisplayMessageEnabled","componentName": "DisplayMessageCtrlr","variableName":"Enabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "DisplayMessageAvailable","componentName": "DisplayMessageCtrlr","variableName":"Available","variableInstance":None,"dataType":"bool","mutability": "ReadOnly", "value": "False"},
    {"ocppName": "NumberOfDisplayMessages","componentName": "DisplayMessageCtrlr","variableName":"DisplayMessages","variableInstance":None,"dataType":"int","mutability": "ReadOnly", "value": 0},
    {"ocppName": "DisplayMessageSupportedFormats","componentName": "DisplayMessageCtrlr","variableName":"SupportedFormats","variableInstance":None,"dataType":"MemberList","mutability": "ReadOnly", "value": set(("ASCII","UTF8"))},
    {"ocppName": "DisplayMessageSupportedPriorities","componentName": "DisplayMessageCtrlr","variableName":"SupportedPriorities","variableInstance":None,"dataType":"MemberList","mutability": "ReadOnly", "value": set(("AlwaysFront",))},
    #Charging Infrastructure related
    #TODO too many component names check after
    #ISO 15118 Related
    {"ocppName": "CentralContractValidationAllowed","componentName": "ISO15118Ctrlr","variableName":"CentralContractValidationAllowed","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ContractValidationOffline","componentName": "ISO15118Ctrlr","variableName":"ContractValidationOffline","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ProtocolSupportedByEV","componentName": "ConnectedEV","variableName":"ProtocolSupportedByEV","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": '''urn:iso:15118:2:2013:MsgDef,2,0'''},
    {"ocppName": "ProtocolAgreed","componentName": "ConnectedEV","variableName":"ProtocolAgreed","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": '''urn:iso:15118:2:2013:MsgDef,2,0'''},
    {"ocppName": "ISO15118PnCEnabled","componentName": "ISO15118Ctrlr","variableName":"PnCEnabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ISO15118V2GCertificateInstallationEnabled","componentName": "ISO15118Ctrlr","variableName":"V2GCertificateInstallationEnabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ISO15118ContractCertificateInstallationEnabled","componentName": "ISO15118Ctrlr","variableName":"ContractCertificateInstallationEnabled","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ISO15118RequestMeteringReceipt","componentName": "ISO15118Ctrlr","variableName":"RequestMeteringReceipt","variableInstance":None,"dataType":"bool","mutability": "ReadWrite", "value": "False"},
    {"ocppName": "ISO15118SeccId","componentName": "ISO15118Ctrlr","variableName":"SeccId","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "TR-ICE-S-0003C4D5578786756453309675436-2"},
    {"ocppName": "ISO15118CountryName","componentName": "ISO15118Ctrlr","variableName":"CountryName","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "TR"},
    {"ocppName": "ISO15118OrganizationName","componentName": "ISO15118Ctrlr","variableName":"OrganizationName","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "Niso"},
    {"ocppName": "ISO15118EvseId","componentName": "ISO15118Ctrlr","variableName":"ISO15118EvseId","variableInstance":None,"dataType":"str","mutability": "ReadWrite", "value": "TR*ICE*E*1234567890*1"},
    ]

async def createVariablesDb():
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()
    try:
        cur.execute('''CREATE TABLE Variables
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ocppName           TEXT    NOT NULL,
            componentName      TEXT    NOT NULL,
            variableName       TEXT    NOT NULL,
            variableInstance   TEXT,
            dataType           TEXT    NOT NULL,
            mutability         TEXT    NOT NULL,
            value              BLOB);''')
    except Exception as e:
        print(e)
    try:
        cur.execute('''CREATE TABLE Reservation
            (
            id                 INTEGER NOT NULL,
            expiryDateTime     TEXT    NOT NULL,
            idToken            TEXT    NOT NULL,
            connectorType      TEXT,
            evseId             TEXT,
            groupIdToken       TEXT);''')
    except Exception as e:
        print(e)
    try:
        cur.execute('''CREATE TABLE NetworkConnectionProfile
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            configurationSlot  INTEGER NOT NULL,
            connectionData     TEXT    NOT NULL);''')
    except Exception as e:
        print(e)
    con.commit()
    con.close()

    await putDefaultVaraiblesIntoTable()

    

async def putDefaultVaraiblesIntoTable():
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()

    for ele in defaultVariables:
        value_arr = []
        for key,value in ele.items():
            value_arr.append(value)
        if(isinstance(value_arr[6],set)):
            stringOfSet = ','.join(value_arr[6])
            if value_arr[3] is None:
                cur.execute('SELECT * FROM Variables WHERE (componentName = :componentName AND variableName = :variableName AND variableInstance IS NULL)',(ele))
                entry = cur.fetchone()
            else:
                cur.execute('SELECT * FROM Variables WHERE (componentName = :componentName AND variableName = :variableName AND variableInstance = :variableInstance)',(ele))
                entry = cur.fetchone()
            if entry is None:
                cur.execute("INSERT INTO Variables(ocppName,componentName,variableName,variableInstance,dataType,mutability,value) VALUES(?,?,?,?,?,?,?)", (value_arr[0],value_arr[1],value_arr[2],value_arr[3],value_arr[4],value_arr[5],stringOfSet))
            else:
                pass
        else:
            if value_arr[3] is None:
                cur.execute('SELECT * FROM Variables WHERE (componentName = :componentName AND variableName = :variableName AND variableInstance IS NULL)',(ele))
                entry = cur.fetchone()
            else:
                cur.execute('SELECT * FROM Variables WHERE (componentName = :componentName AND variableName = :variableName AND variableInstance = :variableInstance)',(ele))
                entry = cur.fetchone()
            if entry is None:
                cur.execute("INSERT INTO Variables (ocppName,componentName,variableName,variableInstance,dataType,mutability,value) VALUES(:ocppName,:componentName,:variableName,:variableInstance,:dataType,:mutability,:value)",(ele))
            else:
                pass
    con.commit()
    con.close()


async def getVariableFromDbById(id):
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()    
    try:
        cur.execute('SELECT ocppName,dataType,value FROM Variables WHERE id = ?',(id,))
        row = cur.fetchone()
        return row
    except:
        return None

async def updateVariableInDb(key,value):
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()    
    try:
        print(value,type(value),isinstance(value,list))
        if(isinstance(value,set) or isinstance(value,list)):
            stringOfSet = ','.join(str(v) for v in value)
            print(stringOfSet,key)
            cur.execute('UPDATE Variables SET value = ? WHERE ocppName = ?',(stringOfSet,key))
        else:
            cur.execute('UPDATE Variables SET value = ? WHERE ocppName = ?',(value,key))
    except Exception as e:
        print(e)
    con.commit()
    con.close()

async def selectVariableFromDb(variable):
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()  
    try:
        if(variable["variableInstance"] == None):
            cur.execute('SELECT * FROM Variables WHERE (componentName = :componentName AND variableName = :variableName AND variableInstance IS NULL)',(variable))
        else:
            cur.execute('SELECT * FROM Variables WHERE (componentName = :componentName AND variableName = :variableName AND variableInstance = :variableInstance)',(variable))
        row = cur.fetchone()
        return row
    except Exception as e:
        print(e)

async def putNetworkProfileIntoDb(slot,data):
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()
    try:
        cur.execute('SELECT * FROM NetworkConnectionProfile WHERE configurationSlot = ?',(slot,))
        entry = cur.fetchone()
        if entry is None:
            print("inserttttttttttttttttttttttt")
            cur.execute("INSERT INTO NetworkConnectionProfile(configurationSlot,connectionData) VALUES(?,?)", (slot,data))
        else:
            print("updateeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            cur.execute("UPDATE NetworkConnectionProfile SET connectionData = ? WHERE configurationSlot = ?", (data,slot))
    except Exception as e:
        print(e)
    con.commit()
    con.close()

async def getNetworkProfileFromDb(slot):
    con = sqlite3.connect("configuration.db")
    cur = con.cursor()
    try:
        cur.execute('SELECT connectionData FROM NetworkConnectionProfile WHERE configurationSlot = ?',(slot,))
        entry = cur.fetchone()
    except:
        pass
    return entry
