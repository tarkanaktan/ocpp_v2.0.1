from dataclasses import dataclass
from typing import List


@dataclass
class CustomData:
    vendorId: str

@dataclass
class Variable:
    name: str
    customData: CustomData = None 
    instance: str = None

@dataclass
class Evse:
    id: int
    customData: CustomData = None
    connectorId: int = None

@dataclass
class Component:
    name: str
    customData: CustomData = None
    evse: Evse = None
    instance: str = None

@dataclass
class Display:
    name: str
    customData: CustomData = None
    evse: Evse = None
    instance: str = None

@dataclass
class Apn:    
    apnAuthentication: str
    apn: str
    apnUserName: str = None
    apnPassword: str = None
    simPin: int = None
    preferredNetwork: str = None
    useOnlyPreferredNetwork: bool = None
    customData: CustomData = None

@dataclass
class MessageContentType:
    content: str
    format: str
    language: str = None
    customData: CustomData = None
 
@dataclass   
class Vpn:
    server: str
    user: str    
    password: str
    key: str
    type: str
    customData: CustomData = None
    group: str = None

@dataclass
class Modem:
    customData: CustomData = None
    iccid: str = None
    imsi: str = None

@dataclass
class StatusInfo:
    reasonCode: str
    additionalInfo: str = None
    customData: CustomData = None

@dataclass
class SignedMeterValue:
    signedMeterData: str
    signingMethod: str
    encodingMethod: str
    publicKey: str
    customData: CustomData = None

@dataclass
class UnitOfMeasure:
    customData: CustomData = None
    unit: str = None
    multiplier: int = None

@dataclass
class SampledValue:
    value: int
    context: str = None
    measurand: str = None
    phase: str = None
    location: str = None
    signedMeterValue: SignedMeterValue = None
    unitOfMeasure: UnitOfMeasure  = None
    customData: CustomData = None

@dataclass
class ACChargingParameters:
    energyAmount: int
    evMinCurrent: int
    evMaxCurrent: int
    evMaxVoltage: int
    customData: CustomData = None

@dataclass
class DCChargingParameters:
    evMaxCurrent: int
    evMaxVoltage: int
    energyAmount: int = None
    evMaxPower: int = None
    stateOfCharge: int = None
    evEnergyCapacity: int = None
    fullSoC: int = None
    bulkSoC: int = None
    CustomData: CustomData = None

@dataclass
class Cost:
    costKind: str
    amount: int
    amountMultiplier: int = None
    CustomData: CustomData = None

@dataclass
class ConsumptionCost:
    startValue: int
    cost: List[Cost]
    CustomData: CustomData = None

@dataclass
class RelativeTimeInterval:
    start: int
    duration: int = None
    CustomData: CustomData = None

@dataclass
class SalesTariffEntry:
    relativeTimeInterval: RelativeTimeInterval
    ePriceLevel: int = None
    consumptionCost: List[ConsumptionCost] = None
    CustomData: CustomData = None

@dataclass
class SalesTariff:
    id: int
    salesTariffEntry: List[SalesTariffEntry]
    salesTariffDescription: str = None
    numEPriceLevels: int = None
    CustomData: CustomData = None

@dataclass
class ChargingSchedulePeriod:
    startPeriod: int
    limit: int
    numberPhases: int = None
    phaseToUse: int = None
    CustomData: CustomData = None

@dataclass
class AdditionalInfoType:
    additionalIdToken: str
    type: str
    CustomData: CustomData = None

@dataclass
class IdToken:
    idToken: str
    type: str
    customData: CustomData = None
    additionalInfo: List[AdditionalInfoType] = None

@dataclass
class IdTokenInfo:
    status: str
    customData: CustomData = None
    cacheExpiryDateTime: str = None
    chargingPriority: int = None
    language1: str = None
    language2: str = None
    evseID: List[int] = None
    groupIdToken: IdToken = None
    personalMessage: MessageContentType = None

@dataclass
class CertificateHashData:
    hashAlgorithm: str
    issuerNameHash: str
    issuerKeyHash: str
    serialNumber: str
    customData: CustomData = None

@dataclass
class ChargingProfileCriterion:
    customData: CustomData = None
    chargingProfilePurpose: str = None
    stackLevel: int = None
    chargingProfileId: List[int] = None
    chargingLimitSource: List[str] = None

@dataclass
class GetVariableData:
    component: Component
    variable: Variable
    customData: CustomData = None
    attributeType: str = None

@dataclass
class Log:
    remoteLocation: str
    customData: CustomData = None
    oldestTimestamp: str = None
    latestTimestamp: str = None

@dataclass
class Message:
    id: int
    priority: str
    message: MessageContentType    
    customData: CustomData = None
    display: Display = None
    state: str = None
    startDateTime: str = None
    endDateTime: str = None
    transactionId: str = None


@dataclass
class ConnectionData:
    ocppVersion: str
    ocppTransport: str
    ocppCsmsUrl: str
    messageTimeout: int
    securityProfile: int
    ocppInterface: str
    customData: CustomData = None
    apn: Apn = None    
    vpn: Vpn = None

@dataclass
class SetMonitoringData:
    value: int
    type: str
    severity: int
    component: Component
    variable: Variable
    customData: CustomData = None
    id: int = None
    transaction: bool = None

@dataclass
class SetVariableData:    
    attributeValue: str
    component: Component
    variable: Variable
    customData: CustomData = None
    attributeType: str = None

@dataclass
class Firmware:    
    location: str
    retrieveDateTime: str
    installDateTime: str = None
    signingCertificate: str = None
    signature: str = None
    customData: CustomData = None

@dataclass
class ChargingStation:
    model: str
    vendorName: str
    serialNumber: str = None
    modem: Modem = None
    firmwareVersion: str = None
    customData: CustomData = None

@dataclass
class ClearMonitoringResult:
    status: str
    id: int
    statusInfo: StatusInfo = None
    customData: CustomData = None

@dataclass
class OCSPRequestData:
    hashAlgorithm: str
    issuerNameHash: str
    issuerKeyHash: str
    serialNumber: str
    responderURL: str
    customData: CustomData = None

@dataclass
class GetVariableResult:
    attributeStatus: str
    component: Component
    variable: Variable
    attributeValue: str = None
    attributeType: str = None
    attributeStatusInfo: StatusInfo = None
    customData: CustomData = None

@dataclass
class MeterValue:
    timestamp: str
    sampledValue: List[SampledValue]
    customData: CustomData = None

@dataclass
class ChargingLimit:
    chargingLimitSource: str
    isGridCritical: bool = None
    customData: CustomData = None

@dataclass
class ChargingNeeds:
    requestedEnergyTransfer: str
    acChargingParameters: ACChargingParameters = None
    dcChargingParameters: DCChargingParameters = None
    departureTime: str = None
    customData: CustomData = None

@dataclass
class ChargingSchedule:
    id: int
    chargingRateUnit: str
    chargingSchedulePeriod: List[ChargingSchedulePeriod]
    startSchedule: str = None
    duration: int = None
    minChargingRate: int = None
    salesTariff: SalesTariff = None
    customData: CustomData = None

@dataclass
class EventData:
    eventId: int
    timestamp: str
    trigger: str
    actualValue: str 
    eventNotificationType: str
    component: Component
    variable: Variable
    variableMonitoringId: int = None
    transactionId: str = None
    cleared: bool = None
    techInfo: str = None
    techCode: str = None
    cause: int = None
    customData: CustomData = None

@dataclass
class ChargingProfileType:
    id: int
    stackLevel: int
    chargingProfilePurpose: str
    chargingProfileKind: str
    chargingSchedule: List[ChargingSchedule]
    recurrencyKind: str = None
    validFrom: str = None
    validTo: str = None
    transactionId: str = None
    customData: CustomData = None

@dataclass
class SetMonitoringResult:
    status: str
    type: str
    severity: int
    component: Component
    variable: Variable
    id: int = None
    statusInfo: StatusInfo  = None
    customData: CustomData = None

@dataclass
class SetVariableResult:
    attributeStatus: str
    component: Component
    variable: Variable
    attributeType: str = None
    attributeStatusInfo: StatusInfo = None
    customData: CustomData = None

@dataclass
class TransactionInfo:
    transactionId: str
    chargingState: str = None
    timeSpentCharging: int = None
    stoppedReason: str = None
    remoteStartId: int = None
    customData: CustomData = None

@dataclass
class CompositeSchedule:
    evseId: int
    duration: int
    scheduleStart: str
    chargingRateUnit: str
    chargingSchedulePeriod: ChargingSchedulePeriod
    customData: CustomData = None

@dataclass
class CertificateHashDataChain:
    certificateType: str
    certificateHashData: CertificateHashData
    customData: CustomData = None
    childCertificateHashData: List[CertificateHashData] = None
@dataclass
class VariableMonitoring:
    id: int
    transaction: bool
    value: int
    type: str
    severity: int
    customData: CustomData = None

@dataclass
class MonitoringData:
    component: Component
    variable: Variable
    variableMonitoring: List[VariableMonitoring]
    CustomData: CustomData = None

@dataclass
class VariableAttribute:
    type: str = None
    value: str = None
    mutability: str = None
    persistent: bool = None
    constant: bool = None
    CustomData: CustomData = None

@dataclass
class VariableCharacteristics:
    dataType: str
    supportsMonitoring: bool
    unit: str = None
    minLimit: int = None
    maxLimit: int = None
    valuesList: str = None
    CustomData: CustomData = None

@dataclass
class ReportData:
    component: Component
    variable: Variable
    variableAttribute: List[VariableAttribute] = None
    variableCharacteristics: VariableCharacteristics = None
    CustomData: CustomData = None

@dataclass
class ClearChargingProfile:
    CustomData: CustomData = None
    evseId: int = None
    chargingProfilePurpose: str = None
    stackLevel: int = None

@dataclass
class ComponentVariable:
    component: Component
    variable: Variable = None
    CustomData: CustomData = None

@dataclass
class AuthorizationData:
    idToken: IdToken
    idTokenInfo: IdTokenInfo = None
    CustomData: CustomData = None
