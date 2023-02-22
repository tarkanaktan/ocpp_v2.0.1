from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class CustomData:
    vendorId: str

@dataclass
class Variable:
    name: str
    customData: CustomData = field(default = None)   
    instance: str = field(default = None)

@dataclass
class Evse:
    id: int
    customData: CustomData = field(default = None)
    connectorId: int = field(default = None)

@dataclass
class Component:
    name: str
    customData: CustomData = field(default = None)
    evse: Evse = field(default = None)
    instance: str = field(default = None)

@dataclass
class Display:
    name: str
    customData: CustomData = field(default = None)
    evse: Evse = field(default = None)
    instance: str = field(default = None)

@dataclass
class Apn:    
    apnAuthentication: str
    apn: str
    apnUserName: str = field(default = None)
    apnPassword: str = field(default = None)
    simPin: int = field(default = None)
    preferredNetwork: str = field(default = None)
    useOnlyPreferredNetwork: bool = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class MessageContentType:
    content: str
    format: str
    language: str = field(default = None)
    customData: CustomData = field(default = None)
 
@dataclass   
class Vpn:
    server: str
    user: str    
    password: str
    key: str
    type: str
    customData: CustomData = field(default = None)
    group: str = field(default = None)

@dataclass
class Modem:
    customData: CustomData = field(default = None)
    iccid: str = field(default = None)
    imsi: str = field(default = None)

@dataclass
class StatusInfo:
    reasonCode: str
    additionalInfo: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class SignedMeterValue:
    signedMeterData: str
    signingMethod: str
    encodingMethod: str
    publicKey: str
    customData: CustomData = field(default = None)

@dataclass
class UnitOfMeasure:
    customData: CustomData = field(default = None)
    unit: str = field(default = None)
    multiplier: int = field(default = None)

@dataclass
class SampledValue:
    value: int
    context: str = field(default = None)
    measurand: str = field(default = None)
    phase: str = field(default = None)
    location: str = field(default = None)
    signedMeterValue: SignedMeterValue = field(default = None)
    unitOfMeasure: UnitOfMeasure  = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class AACChargingParameters:
    energyAmount: int
    evMinCurrent: int
    evMaxCurrent: int
    evMaxVoltage: int
    customData: CustomData = field(default = None)

@dataclass
class DCChargingParameters:
    evMaxCurrent: int
    evMaxVoltage: int
    energyAmount: int = field(default = None)
    evMaxPower: int = field(default = None)
    stateOfCharge: int = field(default = None)
    evEnergyCapacity: int = field(default = None)
    fullSoC: int = field(default = None)
    bulkSoC: int = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class Cost:
    costKind: str
    amount: int
    amountMultiplier: int = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class ConsumptionCost:
    startValue: int
    cost: List[Cost]
    CustomData: CustomData = field(default = None)

@dataclass
class RelativeTimeInterval:
    start: int
    duration: int = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class SalesTariffEntry:
    relativeTimeInterval: RelativeTimeInterval
    ePriceLevel: int = field(default = None)
    consumptionCost: List[ConsumptionCost] = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class SalesTariff:
    id: int
    salesTariffEntry: List[SalesTariffEntry]
    salesTariffDescription: str = field(default = None)
    numEPriceLevels: int = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class ChargingSchedulePeriod:
    startPeriod: int
    limit: int
    numberPhases: int = field(default = None)
    phaseToUse: int = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class AdditionalInfoType:
    additionalIdToken: str
    type: str
    CustomData: CustomData = field(default = None)




@dataclass
class IdToken:
    idToken: str
    type: str
    customData: CustomData = field(default = None)
    additionalInfo: List[AdditionalInfoType] = field(default = None)

@dataclass
class IdTokenInfo:
    status: str
    customData: CustomData = field(default = None)
    cacheExpiryDateTime: str = field(default = None)
    chargingPriority: int = field(default = None)
    language1: str = field(default = None)
    language2: str = field(default = None)
    evseID: List[int] = field(default = None)
    groupIdToken: IdToken = field(default = None)
    personalMessage: MessageContentType = field(default = None)

@dataclass
class CertificateHashData:
    hashAlgorithm: str
    issuerNameHash: str
    issuerKeyHash: str
    serialNumber: str
    customData: CustomData = field(default = None)

@dataclass
class ChargingProfileCriterion:
    customData: CustomData = field(default = None)
    chargingProfilePurpose: str = field(default = None)
    stackLevel: int = field(default = None)
    chargingProfileId: List[int] = field(default = None)
    chargingLimitSource: List[str] = field(default = None)

@dataclass
class GetVariableData:
    component: Component
    variable: Variable
    customData: CustomData = field(default = None)
    attributeType: str = field(default = None)

@dataclass
class Log:
    remoteLocation: str
    customData: CustomData = field(default = None)
    oldestTimestamp: str = field(default = None)
    latestTimestamp: str = field(default = None)

@dataclass
class Message:
    id: int
    priority: str
    message: MessageContentType    
    customData: CustomData = field(default = None)
    display: Display = field(default = None)
    state: str = field(default = None)
    startDateTime: str = field(default = None)
    endDateTime: str = field(default = None)
    transactionId: str = field(default = None)


@dataclass
class ConnectionData:
    ocppVersion: str
    ocppTransport: str
    ocppCsmsUrl: str
    messageTimeout: int
    securityProfile: int
    ocppInterface: str
    customData: CustomData = field(default = None)
    apn: Apn = field(default = None)      
    vpn: Vpn = field(default = None)

@dataclass
class SetMonitoringData:
    value: int
    type: str
    severity: int
    component: Component
    variable: Variable
    customData: CustomData = field(default = None)
    id: int = field(default = None)
    transaction: bool = field(default = None) 

@dataclass
class SetVariableData:    
    attributeValue: str
    component: Component
    variable: Variable
    customData: CustomData = field(default = None) 
    attributeType: str = field(default = None) 

@dataclass
class Firmware:    
    location: str
    retrieveDateTime: str
    installDateTime: str = field(default = None)
    signingCertificate: str = field(default = None)
    signature: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ChargingStation:
    model: str
    vendorName: str
    serialNumber: str = field(default = None)
    modem: Modem = field(default = None)
    firmwareVersion: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ClearMonitoringResult:
    status: str
    id: int
    statusInfo: StatusInfo = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class OCSPRequestData:
    hashAlgorithm: str
    issuerNameHash: str
    issuerKeyHash: str
    serialNumber: str
    responderURL: str
    customData: CustomData = field(default = None)

@dataclass
class GetVariableResult:
    attributeStatus: str
    component: Component
    variable: Variable
    attributeValue: str = field(default = None)
    attributeType: str = field(default = None)
    attributeStatusInfo: StatusInfo = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class MeterValue:
    timestamp: str
    sampledValue: List[SampledValue]
    customData: CustomData = field(default = None) 

@dataclass
class ChargingLimit:
    chargingLimitSource: str
    isGridCritical: bool = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ChargingNeeds:
    requestedEnergyTransfer: str
    acChargingParameters: AACChargingParameters = field(default = None)
    dcChargingParameters: DCChargingParameters = field(default = None)
    departureTime: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ChargingSchedule:
    id: int
    chargingRateUnit: str
    chargingSchedulePeriod: List[ChargingSchedulePeriod]
    startSchedule: str = field(default = None)
    duration: int = field(default = None)
    minChargingRate: int = field(default = None)
    salesTariff: SalesTariff = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class EventData:
    eventId: int
    timestamp: str
    trigger: str
    actualValue: str 
    eventNotificationType: str
    component: Component
    variable: Variable
    variableMonitoringId: int = field(default = None)
    transactionId: str = field(default = None)
    cleared: bool = field(default = None)
    techInfo: str = field(default = None)
    techCode: str = field(default = None)
    cause: int = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class ChargingProfileType:
    id: int
    stackLevel: int
    chargingProfilePurpose: str
    chargingProfileKind: str
    chargingSchedule: List[ChargingSchedule]
    recurrencyKind: str = field(default = None)
    validFrom: str = field(default = None)
    validTo: str = field(default = None)
    transactionId: str = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class SetMonitoringResult:
    status: str
    type: str
    severity: int
    component: Component
    variable: Variable
    id: int = field(default = None)
    statusInfo: StatusInfo  = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class SetVariableResult:
    attributeStatus: str
    component: Component
    variable: Variable
    attributeType: str = field(default = None)
    attributeStatusInfo: StatusInfo = field(default = None)
    customData: CustomData = field(default = None)

@dataclass
class TransactionInfo:
    transactionId: str
    chargingState: str = field(default = None)
    timeSpentCharging: int = field(default = None)
    stoppedReason: str = field(default = None)
    remoteStartId: int = field(default = None) 
    customData: CustomData = field(default = None)

@dataclass
class CompositeSchedule:
    evseId: int
    duration: int
    scheduleStart: str
    chargingRateUnit: str
    chargingSchedulePeriod: ChargingSchedulePeriod
    customData: CustomData = field(default = None)

@dataclass
class CertificateHashDataChain:
    certificateType: str
    certificateHashData: CertificateHashData
    customData: CustomData = field(default = None)
    childCertificateHashData: List[CertificateHashData] = field(default = None)
@dataclass
class VariableMonitoring:
    id: int
    transaction: bool
    value: int
    type: str
    severity: int
    customData: CustomData = field(default = None)

@dataclass
class MonitoringData:
    component: Component
    variable: Variable
    variableMonitoring: List[VariableMonitoring]
    CustomData: CustomData = field(default = None)

@dataclass
class VariableAttribute:
    type: str = field(default = None)
    value: str = field(default = None)
    mutability: str = field(default = None)
    persistent: bool = field(default = None)
    constant: bool = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class VariableCharacteristics:
    dataType: str
    supportsMonitoring: bool
    unit: str = field(default = None)
    minLimit: int = field(default = None)
    maxLimit: int = field(default = None)
    valuesList: str = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class ReportData:
    component: Component
    variable: Variable
    variableAttribute: List[VariableAttribute] = field(default = None)
    variableCharacteristics: VariableCharacteristics = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class ClearChargingProfile:
    CustomData: CustomData = field(default = None)
    evseId: int = field(default = None)
    chargingProfilePurpose: str = field(default = None)
    stackLevel: int = field(default = None)

@dataclass
class ComponentVariable:
    component: Component
    variable: Variable = field(default = None)
    CustomData: CustomData = field(default = None)

@dataclass
class AuthorizationData:
    idToken: IdToken
    idTokenInfo: IdTokenInfo = field(default = None)
    CustomData: CustomData = field(default = None)

    




























    

































    


























