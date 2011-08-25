# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""This package shows all the root level subpackage dependencies of the combined CIM model.
"""

from CIM15.CombinedVersion import CombinedVersion
from CIM15.Element import Element
from CIM15.Stereotype import Stereotype
from CIM15.Package import Package

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15"
nsPrefix = "cim"

packageMap = {
    "CombinedVersion": "CIM15",
    "Element": "CIM15",
    "Stereotype": "CIM15",
    "Package": "CIM15",
    "IEC61970CIMVersion": "CIM15.IEC61970",
    "RemoteSource": "CIM15.IEC61970.SCADA",
    "RemotePoint": "CIM15.IEC61970.SCADA",
    "RemoteUnit": "CIM15.IEC61970.SCADA",
    "RemoteControl": "CIM15.IEC61970.SCADA",
    "CommunicationLink": "CIM15.IEC61970.SCADA",
    "Reservoir": "CIM15.IEC61970.Generation.Production",
    "CogenerationPlant": "CIM15.IEC61970.Generation.Production",
    "GenUnitOpSchedule": "CIM15.IEC61970.Generation.Production",
    "FuelAllocationSchedule": "CIM15.IEC61970.Generation.Production",
    "GrossToNetActivePowerCurve": "CIM15.IEC61970.Generation.Production",
    "LevelVsVolumeCurve": "CIM15.IEC61970.Generation.Production",
    "StartRampCurve": "CIM15.IEC61970.Generation.Production",
    "NuclearGeneratingUnit": "CIM15.IEC61970.Generation.Production",
    "EmissionCurve": "CIM15.IEC61970.Generation.Production",
    "HydroPumpOpSchedule": "CIM15.IEC61970.Generation.Production",
    "SteamSendoutSchedule": "CIM15.IEC61970.Generation.Production",
    "TargetLevelSchedule": "CIM15.IEC61970.Generation.Production",
    "CombinedCyclePlant": "CIM15.IEC61970.Generation.Production",
    "HeatRateCurve": "CIM15.IEC61970.Generation.Production",
    "ThermalGeneratingUnit": "CIM15.IEC61970.Generation.Production",
    "EmissionAccount": "CIM15.IEC61970.Generation.Production",
    "PenstockLossCurve": "CIM15.IEC61970.Generation.Production",
    "StartupModel": "CIM15.IEC61970.Generation.Production",
    "HydroGeneratingUnit": "CIM15.IEC61970.Generation.Production",
    "GenUnitOpCostCurve": "CIM15.IEC61970.Generation.Production",
    "IncrementalHeatRateCurve": "CIM15.IEC61970.Generation.Production",
    "FossilFuel": "CIM15.IEC61970.Generation.Production",
    "GeneratingUnit": "CIM15.IEC61970.Generation.Production",
    "StartIgnFuelCurve": "CIM15.IEC61970.Generation.Production",
    "StartMainFuelCurve": "CIM15.IEC61970.Generation.Production",
    "TailbayLossCurve": "CIM15.IEC61970.Generation.Production",
    "HydroPump": "CIM15.IEC61970.Generation.Production",
    "InflowForecast": "CIM15.IEC61970.Generation.Production",
    "HydroGeneratingEfficiencyCurve": "CIM15.IEC61970.Generation.Production",
    "ShutdownCurve": "CIM15.IEC61970.Generation.Production",
    "HydroPowerPlant": "CIM15.IEC61970.Generation.Production",
    "CAESPlant": "CIM15.IEC61970.Generation.Production",
    "AirCompressor": "CIM15.IEC61970.Generation.Production",
    "HeatInputCurve": "CIM15.IEC61970.Generation.Production",
    "WindGeneratingUnit": "CIM15.IEC61970.Generation.Production",
    "BWRSteamSupply": "CIM15.IEC61970.Generation.GenerationDynamics",
    "HydroTurbine": "CIM15.IEC61970.Generation.GenerationDynamics",
    "SteamTurbine": "CIM15.IEC61970.Generation.GenerationDynamics",
    "SteamSupply": "CIM15.IEC61970.Generation.GenerationDynamics",
    "FossilSteamSupply": "CIM15.IEC61970.Generation.GenerationDynamics",
    "Subcritical": "CIM15.IEC61970.Generation.GenerationDynamics",
    "PWRSteamSupply": "CIM15.IEC61970.Generation.GenerationDynamics",
    "PrimeMover": "CIM15.IEC61970.Generation.GenerationDynamics",
    "CombustionTurbine": "CIM15.IEC61970.Generation.GenerationDynamics",
    "HeatRecoveryBoiler": "CIM15.IEC61970.Generation.GenerationDynamics",
    "Supercritical": "CIM15.IEC61970.Generation.GenerationDynamics",
    "DrumBoiler": "CIM15.IEC61970.Generation.GenerationDynamics",
    "CTTempActivePowerCurve": "CIM15.IEC61970.Generation.GenerationDynamics",
    "EquipmentItem": "CIM15.IEC61970.Informative.InfWork",
    "Appointment": "CIM15.IEC61970.Informative.InfWork",
    "WorkStatusEntry": "CIM15.IEC61970.Informative.InfWork",
    "BusinessCase": "CIM15.IEC61970.Informative.InfWork",
    "TypeMaterial": "CIM15.IEC61970.Informative.InfWork",
    "DesignLocation": "CIM15.IEC61970.Informative.InfWork",
    "OverheadCost": "CIM15.IEC61970.Informative.InfWork",
    "Crew": "CIM15.IEC61970.Informative.InfWork",
    "DiagnosisDataSet": "CIM15.IEC61970.Informative.InfWork",
    "CUAsset": "CIM15.IEC61970.Informative.InfWork",
    "Request": "CIM15.IEC61970.Informative.InfWork",
    "Design": "CIM15.IEC61970.Informative.InfWork",
    "WorkTask": "CIM15.IEC61970.Informative.InfWork",
    "ConditionFactor": "CIM15.IEC61970.Informative.InfWork",
    "QualificationRequirement": "CIM15.IEC61970.Informative.InfWork",
    "WorkLocation": "CIM15.IEC61970.Informative.InfWork",
    "CostType": "CIM15.IEC61970.Informative.InfWork",
    "CUMaterialItem": "CIM15.IEC61970.Informative.InfWork",
    "PropertyUnit": "CIM15.IEC61970.Informative.InfWork",
    "Project": "CIM15.IEC61970.Informative.InfWork",
    "CULaborItem": "CIM15.IEC61970.Informative.InfWork",
    "LaborItem": "CIM15.IEC61970.Informative.InfWork",
    "WorkFlowStep": "CIM15.IEC61970.Informative.InfWork",
    "InspectionDataSet": "CIM15.IEC61970.Informative.InfWork",
    "WorkCostDetail": "CIM15.IEC61970.Informative.InfWork",
    "CompatibleUnit": "CIM15.IEC61970.Informative.InfWork",
    "WorkCostSummary": "CIM15.IEC61970.Informative.InfWork",
    "NonStandardItem": "CIM15.IEC61970.Informative.InfWork",
    "InfoQuestion": "CIM15.IEC61970.Informative.InfWork",
    "Regulation": "CIM15.IEC61970.Informative.InfWork",
    "ContractorItem": "CIM15.IEC61970.Informative.InfWork",
    "CUAllowableAction": "CIM15.IEC61970.Informative.InfWork",
    "CULaborCode": "CIM15.IEC61970.Informative.InfWork",
    "AccessPermit": "CIM15.IEC61970.Informative.InfWork",
    "CUWorkEquipmentItem": "CIM15.IEC61970.Informative.InfWork",
    "DesignLocationCU": "CIM15.IEC61970.Informative.InfWork",
    "MaintenanceDataSet": "CIM15.IEC61970.Informative.InfWork",
    "MiscCostItem": "CIM15.IEC61970.Informative.InfWork",
    "MaterialItem": "CIM15.IEC61970.Informative.InfWork",
    "ShiftPattern": "CIM15.IEC61970.Informative.InfWork",
    "Capability": "CIM15.IEC61970.Informative.InfWork",
    "Usage": "CIM15.IEC61970.Informative.InfWork",
    "OneCallRequest": "CIM15.IEC61970.Informative.InfWork",
    "Assignment": "CIM15.IEC61970.Informative.InfWork",
    "CUContractorItem": "CIM15.IEC61970.Informative.InfWork",
    "CUGroup": "CIM15.IEC61970.Informative.InfWork",
    "ErpRecDelvLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpLedgerBudget": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpTimeEntry": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpCompetency": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPurchaseOrder": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpEngChangeOrder": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpProjectAccounting": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpRecLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPayableLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpLedBudLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpRequisition": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpOrganisation": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpInvoice": "CIM15.IEC61970.Informative.InfERPSupport",
    "DocErpPersonRole": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpBankAccount": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpQuote": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPerson": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpItemMaster": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpBOM": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpInventoryCount": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpIssueInventory": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPayable": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpLedger": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPOLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpLedgerEntry": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPayment": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpReceivable": "CIM15.IEC61970.Informative.InfERPSupport",
    "DocOrgRole": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpReqLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpTimeSheet": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpInventory": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpChartOfAccounts": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpSiteLevelData": "CIM15.IEC61970.Informative.InfERPSupport",
    "OrgErpPersonRole": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpReceiveDelivery": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpSalesOrder": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpJournalEntry": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpInvoiceLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "OrgOrgRole": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpJournal": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpPersonnel": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpQuoteLineItem": "CIM15.IEC61970.Informative.InfERPSupport",
    "ErpBomItemData": "CIM15.IEC61970.Informative.InfERPSupport",
    "Role": "CIM15.IEC61970.Informative.InfCommon",
    "Bank": "CIM15.IEC61970.Informative.InfCommon",
    "Skill": "CIM15.IEC61970.Informative.InfCommon",
    "BusinessRole": "CIM15.IEC61970.Informative.InfCommon",
    "ScheduledEvent": "CIM15.IEC61970.Informative.InfCommon",
    "ScheduleParameterInfo": "CIM15.IEC61970.Informative.InfCommon",
    "DocPsrRole": "CIM15.IEC61970.Informative.InfCommon",
    "Ratio": "CIM15.IEC61970.Informative.InfCommon",
    "BankAccount": "CIM15.IEC61970.Informative.InfCommon",
    "Craft": "CIM15.IEC61970.Informative.InfCommon",
    "DocDocRole": "CIM15.IEC61970.Informative.InfCommon",
    "BusinessPlan": "CIM15.IEC61970.Informative.InfCommon",
    "FACTSDevice": "CIM15.IEC61970.Informative.InfAssets",
    "DocAssetRole": "CIM15.IEC61970.Informative.InfAssets",
    "DuctBank": "CIM15.IEC61970.Informative.InfAssets",
    "ConductorAsset": "CIM15.IEC61970.Informative.InfAssets",
    "FinancialInfo": "CIM15.IEC61970.Informative.InfAssets",
    "ProtectionEquipmentInfo": "CIM15.IEC61970.Informative.InfAssets",
    "ProcedureDataSet": "CIM15.IEC61970.Informative.InfAssets",
    "WindingInsulation": "CIM15.IEC61970.Informative.InfAssets",
    "Specification": "CIM15.IEC61970.Informative.InfAssets",
    "UndergroundStructure": "CIM15.IEC61970.Informative.InfAssets",
    "PotentialTransformerInfo": "CIM15.IEC61970.Informative.InfAssets",
    "Structure": "CIM15.IEC61970.Informative.InfAssets",
    "CurrentTransformerInfo": "CIM15.IEC61970.Informative.InfAssets",
    "BushingInsulationPF": "CIM15.IEC61970.Informative.InfAssets",
    "Joint": "CIM15.IEC61970.Informative.InfAssets",
    "ElectricalInfo": "CIM15.IEC61970.Informative.InfAssets",
    "WorkEquipment": "CIM15.IEC61970.Informative.InfAssets",
    "FaultIndicatorInfo": "CIM15.IEC61970.Informative.InfAssets",
    "Duct": "CIM15.IEC61970.Informative.InfAssets",
    "PowerRating": "CIM15.IEC61970.Informative.InfAssets",
    "AssetAssetRole": "CIM15.IEC61970.Informative.InfAssets",
    "TransformerAsset": "CIM15.IEC61970.Informative.InfAssets",
    "Procedure": "CIM15.IEC61970.Informative.InfAssets",
    "BreakerInfo": "CIM15.IEC61970.Informative.InfAssets",
    "CompositeSwitchInfo": "CIM15.IEC61970.Informative.InfAssets",
    "Cabinet": "CIM15.IEC61970.Informative.InfAssets",
    "Bushing": "CIM15.IEC61970.Informative.InfAssets",
    "Vehicle": "CIM15.IEC61970.Informative.InfAssets",
    "SurgeProtectorInfo": "CIM15.IEC61970.Informative.InfAssets",
    "StructureSupport": "CIM15.IEC61970.Informative.InfAssets",
    "ComEquipment": "CIM15.IEC61970.Informative.InfAssets",
    "AssetPropertyCurve": "CIM15.IEC61970.Informative.InfAssets",
    "FailureEvent": "CIM15.IEC61970.Informative.InfAssets",
    "DimensionsInfo": "CIM15.IEC61970.Informative.InfAssets",
    "Tower": "CIM15.IEC61970.Informative.InfAssets",
    "MountingConnection": "CIM15.IEC61970.Informative.InfAssets",
    "Medium": "CIM15.IEC61970.Informative.InfAssets",
    "RecloserInfo": "CIM15.IEC61970.Informative.InfAssets",
    "Facility": "CIM15.IEC61970.Informative.InfAssets",
    "ShuntImpedanceInfo": "CIM15.IEC61970.Informative.InfAssets",
    "ShuntCompensatorInfo": "CIM15.IEC61970.Informative.InfAssets",
    "MountingPoint": "CIM15.IEC61970.Informative.InfAssets",
    "SubstationAsset": "CIM15.IEC61970.Informative.InfAssets",
    "Streetlight": "CIM15.IEC61970.Informative.InfAssets",
    "Tool": "CIM15.IEC61970.Informative.InfAssets",
    "SVC": "CIM15.IEC61970.Informative.InfAssets",
    "OrgAssetRole": "CIM15.IEC61970.Informative.InfAssets",
    "TestDataSet": "CIM15.IEC61970.Informative.InfAssets",
    "GenericAssetModelOrMaterial": "CIM15.IEC61970.Informative.InfAssets",
    "ReliabilityInfo": "CIM15.IEC61970.Informative.InfAssets",
    "TransformerObservation": "CIM15.IEC61970.Informative.InfAssets",
    "Pole": "CIM15.IEC61970.Informative.InfAssets",
    "SwitchInfo": "CIM15.IEC61970.Informative.InfAssets",
    "StandardIndustryCode": "CIM15.IEC61970.Informative.InfCustomers",
    "OutageHistory": "CIM15.IEC61970.Informative.InfCustomers",
    "ComplianceEvent": "CIM15.IEC61970.Informative.InfCustomers",
    "CustomerBillingInfo": "CIM15.IEC61970.Informative.InfCustomers",
    "ServiceGuarantee": "CIM15.IEC61970.Informative.InfCustomers",
    "SubscribePowerCurve": "CIM15.IEC61970.Informative.InfCustomers",
    "ExternalCustomerAgreement": "CIM15.IEC61970.Informative.InfCustomers",
    "PowerQualityPricing": "CIM15.IEC61970.Informative.InfCustomers",
    "WorkBillingInfo": "CIM15.IEC61970.Informative.InfCustomers",
    "OutageRecord": "CIM15.IEC61970.Informative.InfOperations",
    "OutageReport": "CIM15.IEC61970.Informative.InfOperations",
    "ChangeItem": "CIM15.IEC61970.Informative.InfOperations",
    "PSREvent": "CIM15.IEC61970.Informative.InfOperations",
    "PlannedOutage": "CIM15.IEC61970.Informative.InfOperations",
    "CircuitSection": "CIM15.IEC61970.Informative.InfOperations",
    "SafetyDocument": "CIM15.IEC61970.Informative.InfOperations",
    "OperationalRestriction": "CIM15.IEC61970.Informative.InfOperations",
    "ChangeSet": "CIM15.IEC61970.Informative.InfOperations",
    "SwitchingSchedule": "CIM15.IEC61970.Informative.InfOperations",
    "Circuit": "CIM15.IEC61970.Informative.InfOperations",
    "NetworkDataSet": "CIM15.IEC61970.Informative.InfOperations",
    "OutageStep": "CIM15.IEC61970.Informative.InfOperations",
    "OrgPsrRole": "CIM15.IEC61970.Informative.InfOperations",
    "OutageCode": "CIM15.IEC61970.Informative.InfOperations",
    "IncidentCode": "CIM15.IEC61970.Informative.InfOperations",
    "LandBase": "CIM15.IEC61970.Informative.InfOperations",
    "ErpPersonScheduleStepRole": "CIM15.IEC61970.Informative.InfOperations",
    "SwitchingStep": "CIM15.IEC61970.Informative.InfOperations",
    "CallBack": "CIM15.IEC61970.Informative.InfOperations",
    "TroubleTicket": "CIM15.IEC61970.Informative.InfOperations",
    "IncidentRecord": "CIM15.IEC61970.Informative.InfOperations",
    "OutageNotification": "CIM15.IEC61970.Informative.InfOperations",
    "OutageStepPsrRole": "CIM15.IEC61970.Informative.InfOperations",
    "LocationGrant": "CIM15.IEC61970.Informative.InfLocations",
    "RightOfWay": "CIM15.IEC61970.Informative.InfLocations",
    "PersonPropertyRole": "CIM15.IEC61970.Informative.InfLocations",
    "Zone": "CIM15.IEC61970.Informative.InfLocations",
    "RedLine": "CIM15.IEC61970.Informative.InfLocations",
    "Route": "CIM15.IEC61970.Informative.InfLocations",
    "OrgPropertyRole": "CIM15.IEC61970.Informative.InfLocations",
    "Direction": "CIM15.IEC61970.Informative.InfLocations",
    "LandProperty": "CIM15.IEC61970.Informative.InfLocations",
    "Hazard": "CIM15.IEC61970.Informative.InfLocations",
    "GmlFeatureType": "CIM15.IEC61970.Informative.InfGMLSupport",
    "Map": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlPointGeometry": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlHalo": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlColour": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlFont": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlPolygonSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlStroke": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlBaseSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlPosition": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlTextSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlPolygonGeometry": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlObservation": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlMark": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlGraphic": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlLabelPlacement": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlGeometryStyle": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlLineGeometry": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlValue": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlLineSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlDiagramObject": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlPointSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlTopologyStyle": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlSelector": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlSvgParameter": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlLabelStyle": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlFill": "CIM15.IEC61970.Informative.InfGMLSupport",
    "Diagram": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlFeatureStyle": "CIM15.IEC61970.Informative.InfGMLSupport",
    "GmlRasterSymbol": "CIM15.IEC61970.Informative.InfGMLSupport",
    "ModelingAuthority": "CIM15.IEC61970.Informative.InfCore",
    "ModelingAuthoritySet": "CIM15.IEC61970.Informative.InfCore",
    "LoadMgmtRecord": "CIM15.IEC61970.Informative.InfLoadControl",
    "LoadShedFunction": "CIM15.IEC61970.Informative.InfLoadControl",
    "LoadMgmtFunction": "CIM15.IEC61970.Informative.InfLoadControl",
    "LoadLimitFunction": "CIM15.IEC61970.Informative.InfLoadControl",
    "GasMeteringFunction": "CIM15.IEC61970.Informative.InfMetering",
    "WaterMeteringFunction": "CIM15.IEC61970.Informative.InfMetering",
    "AssetModelCatalogue": "CIM15.IEC61970.Informative.InfAssetModels",
    "TransformerAssetModel": "CIM15.IEC61970.Informative.InfAssetModels",
    "AssetModelCatalogueItem": "CIM15.IEC61970.Informative.InfAssetModels",
    "TypeAssetCatalogue": "CIM15.IEC61970.Informative.InfTypeAsset",
    "GeneratorTypeAsset": "CIM15.IEC61970.Informative.InfTypeAsset",
    "SvVoltage": "CIM15.IEC61970.StateVariables",
    "SvShortCircuit": "CIM15.IEC61970.StateVariables",
    "SvShuntCompensatorSections": "CIM15.IEC61970.StateVariables",
    "StateVariable": "CIM15.IEC61970.StateVariables",
    "SvTapStep": "CIM15.IEC61970.StateVariables",
    "SvStatus": "CIM15.IEC61970.StateVariables",
    "SvInjection": "CIM15.IEC61970.StateVariables",
    "SvPowerFlow": "CIM15.IEC61970.StateVariables",
    "TopologicalIsland": "CIM15.IEC61970.StateVariables",
    "PhaseImpedanceData": "CIM15.IEC61970.Wires",
    "TapSchedule": "CIM15.IEC61970.Wires",
    "TransformerStarImpedance": "CIM15.IEC61970.Wires",
    "Recloser": "CIM15.IEC61970.Wires",
    "RatioTapChangerTabularPoint": "CIM15.IEC61970.Wires",
    "PhaseTapChangerTabular": "CIM15.IEC61970.Wires",
    "RatioTapChanger": "CIM15.IEC61970.Wires",
    "PhaseTapChangerLinear": "CIM15.IEC61970.Wires",
    "ACLineSegment": "CIM15.IEC61970.Wires",
    "PowerTransformerEnd": "CIM15.IEC61970.Wires",
    "Junction": "CIM15.IEC61970.Wires",
    "RegulatingCondEq": "CIM15.IEC61970.Wires",
    "Sectionaliser": "CIM15.IEC61970.Wires",
    "RatioTapChangerTabular": "CIM15.IEC61970.Wires",
    "PowerTransformer": "CIM15.IEC61970.Wires",
    "Fuse": "CIM15.IEC61970.Wires",
    "EnergyConsumer": "CIM15.IEC61970.Wires",
    "Disconnector": "CIM15.IEC61970.Wires",
    "Connector": "CIM15.IEC61970.Wires",
    "ReactiveCapabilityCurve": "CIM15.IEC61970.Wires",
    "Plant": "CIM15.IEC61970.Wires",
    "GroundDisconnector": "CIM15.IEC61970.Wires",
    "Resistor": "CIM15.IEC61970.Wires",
    "SynchronousMachine": "CIM15.IEC61970.Wires",
    "PhaseTapChangerAsymetrical": "CIM15.IEC61970.Wires",
    "RectifierInverter": "CIM15.IEC61970.Wires",
    "SeriesCompensator": "CIM15.IEC61970.Wires",
    "TapChangerControl": "CIM15.IEC61970.Wires",
    "RegulatingControl": "CIM15.IEC61970.Wires",
    "ProtectedSwitch": "CIM15.IEC61970.Wires",
    "PhaseTapChanger": "CIM15.IEC61970.Wires",
    "Ground": "CIM15.IEC61970.Wires",
    "CompositeSwitch": "CIM15.IEC61970.Wires",
    "RegulationSchedule": "CIM15.IEC61970.Wires",
    "TransformerTankEnd": "CIM15.IEC61970.Wires",
    "Breaker": "CIM15.IEC61970.Wires",
    "MutualCoupling": "CIM15.IEC61970.Wires",
    "Line": "CIM15.IEC61970.Wires",
    "PerLengthPhaseImpedance": "CIM15.IEC61970.Wires",
    "FrequencyConverter": "CIM15.IEC61970.Wires",
    "ShuntCompensator": "CIM15.IEC61970.Wires",
    "VoltageControlZone": "CIM15.IEC61970.Wires",
    "LoadBreakSwitch": "CIM15.IEC61970.Wires",
    "BusbarSection": "CIM15.IEC61970.Wires",
    "TransformerEnd": "CIM15.IEC61970.Wires",
    "TransformerCoreAdmittance": "CIM15.IEC61970.Wires",
    "StaticVarCompensator": "CIM15.IEC61970.Wires",
    "Switch": "CIM15.IEC61970.Wires",
    "PerLengthSequenceImpedance": "CIM15.IEC61970.Wires",
    "TransformerMeshImpedance": "CIM15.IEC61970.Wires",
    "SwitchSchedule": "CIM15.IEC61970.Wires",
    "EnergySource": "CIM15.IEC61970.Wires",
    "TransformerTank": "CIM15.IEC61970.Wires",
    "PhaseTapChangerTabularPoint": "CIM15.IEC61970.Wires",
    "DCLineSegment": "CIM15.IEC61970.Wires",
    "TapChanger": "CIM15.IEC61970.Wires",
    "Conductor": "CIM15.IEC61970.Wires",
    "PhaseTapChangerNonLinear": "CIM15.IEC61970.Wires",
    "PhaseTapChangerSymetrical": "CIM15.IEC61970.Wires",
    "Jumper": "CIM15.IEC61970.Wires",
    "AccumulatorLimit": "CIM15.IEC61970.Meas",
    "ValueToAlias": "CIM15.IEC61970.Meas",
    "MeasurementValueSource": "CIM15.IEC61970.Meas",
    "Analog": "CIM15.IEC61970.Meas",
    "AnalogValue": "CIM15.IEC61970.Meas",
    "Measurement": "CIM15.IEC61970.Meas",
    "ControlType": "CIM15.IEC61970.Meas",
    "StringMeasurementValue": "CIM15.IEC61970.Meas",
    "StringMeasurement": "CIM15.IEC61970.Meas",
    "AnalogLimit": "CIM15.IEC61970.Meas",
    "SetPoint": "CIM15.IEC61970.Meas",
    "Limit": "CIM15.IEC61970.Meas",
    "Discrete": "CIM15.IEC61970.Meas",
    "ValueAliasSet": "CIM15.IEC61970.Meas",
    "Quality61850": "CIM15.IEC61970.Meas",
    "AccumulatorValue": "CIM15.IEC61970.Meas",
    "Command": "CIM15.IEC61970.Meas",
    "Accumulator": "CIM15.IEC61970.Meas",
    "MeasurementValueQuality": "CIM15.IEC61970.Meas",
    "MeasurementValue": "CIM15.IEC61970.Meas",
    "DiscreteValue": "CIM15.IEC61970.Meas",
    "AnalogLimitSet": "CIM15.IEC61970.Meas",
    "LimitSet": "CIM15.IEC61970.Meas",
    "AccumulatorLimitSet": "CIM15.IEC61970.Meas",
    "Control": "CIM15.IEC61970.Meas",
    "ConformLoad": "CIM15.IEC61970.LoadModel",
    "ConformLoadGroup": "CIM15.IEC61970.LoadModel",
    "SeasonDayTypeSchedule": "CIM15.IEC61970.LoadModel",
    "LoadGroup": "CIM15.IEC61970.LoadModel",
    "ConformLoadSchedule": "CIM15.IEC61970.LoadModel",
    "LoadArea": "CIM15.IEC61970.LoadModel",
    "PowerCutZone": "CIM15.IEC61970.LoadModel",
    "LoadResponseCharacteristic": "CIM15.IEC61970.LoadModel",
    "NonConformLoad": "CIM15.IEC61970.LoadModel",
    "StationSupply": "CIM15.IEC61970.LoadModel",
    "EnergyArea": "CIM15.IEC61970.LoadModel",
    "NonConformLoadSchedule": "CIM15.IEC61970.LoadModel",
    "NonConformLoadGroup": "CIM15.IEC61970.LoadModel",
    "DayType": "CIM15.IEC61970.LoadModel",
    "SubLoadArea": "CIM15.IEC61970.LoadModel",
    "Season": "CIM15.IEC61970.LoadModel",
    "SwitchPhase": "CIM15.IEC61970.WiresPhaseModel",
    "ShuntCompensatorPhase": "CIM15.IEC61970.WiresPhaseModel",
    "EnergyConsumerPhase": "CIM15.IEC61970.WiresPhaseModel",
    "AltTieMeas": "CIM15.IEC61970.ControlArea",
    "AltGeneratingUnitMeas": "CIM15.IEC61970.ControlArea",
    "TieFlow": "CIM15.IEC61970.ControlArea",
    "ControlArea": "CIM15.IEC61970.ControlArea",
    "ControlAreaGeneratingUnit": "CIM15.IEC61970.ControlArea",
    "PotentialTransformer": "CIM15.IEC61970.AuxiliaryEquipment",
    "Sensor": "CIM15.IEC61970.AuxiliaryEquipment",
    "AuxiliaryEquipment": "CIM15.IEC61970.AuxiliaryEquipment",
    "CurrentTransformer": "CIM15.IEC61970.AuxiliaryEquipment",
    "SurgeProtector": "CIM15.IEC61970.AuxiliaryEquipment",
    "FaultIndicator": "CIM15.IEC61970.AuxiliaryEquipment",
    "DateTimeInterval": "CIM15.IEC61970.Domain",
    "PowerSystemResource": "CIM15.IEC61970.Core",
    "NameTypeAuthority": "CIM15.IEC61970.Core",
    "Equipment": "CIM15.IEC61970.Core",
    "ConductingEquipment": "CIM15.IEC61970.Core",
    "RegularTimePoint": "CIM15.IEC61970.Core",
    "ConnectivityNode": "CIM15.IEC61970.Core",
    "PSRType": "CIM15.IEC61970.Core",
    "ConnectivityNodeContainer": "CIM15.IEC61970.Core",
    "Bay": "CIM15.IEC61970.Core",
    "EquipmentContainer": "CIM15.IEC61970.Core",
    "ReportingGroup": "CIM15.IEC61970.Core",
    "BasePower": "CIM15.IEC61970.Core",
    "PsrList": "CIM15.IEC61970.Core",
    "IdentifiedObject": "CIM15.IEC61970.Core",
    "BasicIntervalSchedule": "CIM15.IEC61970.Core",
    "Curve": "CIM15.IEC61970.Core",
    "GeographicalRegion": "CIM15.IEC61970.Core",
    "CurveData": "CIM15.IEC61970.Core",
    "SubGeographicalRegion": "CIM15.IEC61970.Core",
    "NameType": "CIM15.IEC61970.Core",
    "Substation": "CIM15.IEC61970.Core",
    "Name": "CIM15.IEC61970.Core",
    "BaseVoltage": "CIM15.IEC61970.Core",
    "Terminal": "CIM15.IEC61970.Core",
    "IrregularIntervalSchedule": "CIM15.IEC61970.Core",
    "RegularIntervalSchedule": "CIM15.IEC61970.Core",
    "OperatingParticipant": "CIM15.IEC61970.Core",
    "OperatingShare": "CIM15.IEC61970.Core",
    "VoltageLevel": "CIM15.IEC61970.Core",
    "ReportingSuperGroup": "CIM15.IEC61970.Core",
    "IrregularTimePoint": "CIM15.IEC61970.Core",
    "TextDiagramObject": "CIM15.IEC61970.Graphics",
    "DiagramObjectGluePoint": "CIM15.IEC61970.Graphics",
    "DiagramObject": "CIM15.IEC61970.Graphics",
    "DiagramObjectStyle": "CIM15.IEC61970.Graphics",
    "DiagramObjectPoint": "CIM15.IEC61970.Graphics",
    "VisibilityLayer": "CIM15.IEC61970.Graphics",
    "ApparentPowerLimit": "CIM15.IEC61970.OperationalLimits",
    "ActivePowerLimit": "CIM15.IEC61970.OperationalLimits",
    "OperationalLimitType": "CIM15.IEC61970.OperationalLimits",
    "BranchGroup": "CIM15.IEC61970.OperationalLimits",
    "OperationalLimitSet": "CIM15.IEC61970.OperationalLimits",
    "ActivePowerLimitSet": "CIM15.IEC61970.OperationalLimits",
    "CurrentLimit": "CIM15.IEC61970.OperationalLimits",
    "CurrentLimitSet": "CIM15.IEC61970.OperationalLimits",
    "ApparentPowerLimitSet": "CIM15.IEC61970.OperationalLimits",
    "BranchGroupTerminal": "CIM15.IEC61970.OperationalLimits",
    "VoltageLimitSet": "CIM15.IEC61970.OperationalLimits",
    "VoltageLimit": "CIM15.IEC61970.OperationalLimits",
    "OperationalLimit": "CIM15.IEC61970.OperationalLimits",
    "SwitchingOperation": "CIM15.IEC61970.Outage",
    "OutageSchedule": "CIM15.IEC61970.Outage",
    "ClearanceTagType": "CIM15.IEC61970.Outage",
    "ClearanceTag": "CIM15.IEC61970.Outage",
    "Cut": "CIM15.IEC61970.CutsJumpers",
    "Clamp": "CIM15.IEC61970.CutsJumpers",
    "RecloseSequence": "CIM15.IEC61970.Protection",
    "SynchrocheckRelay": "CIM15.IEC61970.Protection",
    "CurrentRelay": "CIM15.IEC61970.Protection",
    "ProtectionEquipment": "CIM15.IEC61970.Protection",
    "EquivalentShunt": "CIM15.IEC61970.Equivalents",
    "EquivalentEquipment": "CIM15.IEC61970.Equivalents",
    "EquivalentNetwork": "CIM15.IEC61970.Equivalents",
    "EquivalentInjection": "CIM15.IEC61970.Equivalents",
    "EquivalentBranch": "CIM15.IEC61970.Equivalents",
    "ContingencyEquipment": "CIM15.IEC61970.Contingency",
    "Contingency": "CIM15.IEC61970.Contingency",
    "ContingencyElement": "CIM15.IEC61970.Contingency",
    "BusNameMarker": "CIM15.IEC61970.Topology",
    "TopologicalNode": "CIM15.IEC61970.Topology",
    "IEC61968CIMVersion": "CIM15.IEC61968",
    "PostalAddress": "CIM15.IEC61968.Common",
    "Status": "CIM15.IEC61968.Common",
    "ElectronicAddress": "CIM15.IEC61968.Common",
    "Location": "CIM15.IEC61968.Common",
    "TownDetail": "CIM15.IEC61968.Common",
    "CoordinateSystem": "CIM15.IEC61968.Common",
    "Document": "CIM15.IEC61968.Common",
    "PositionPoint": "CIM15.IEC61968.Common",
    "UserAttribute": "CIM15.IEC61968.Common",
    "StreetAddress": "CIM15.IEC61968.Common",
    "StreetDetail": "CIM15.IEC61968.Common",
    "TimeSchedule": "CIM15.IEC61968.Common",
    "ActivityRecord": "CIM15.IEC61968.Common",
    "TimePoint": "CIM15.IEC61968.Common",
    "Organisation": "CIM15.IEC61968.Common",
    "TelephoneNumber": "CIM15.IEC61968.Common",
    "Agreement": "CIM15.IEC61968.Common",
    "ShortCircuitTest": "CIM15.IEC61968.AssetModels",
    "EndDeviceInfo": "CIM15.IEC61968.AssetModels",
    "WireType": "CIM15.IEC61968.AssetModels",
    "TapeShieldCableInfo": "CIM15.IEC61968.AssetModels",
    "ConductorInfo": "CIM15.IEC61968.AssetModels",
    "TapChangerInfo": "CIM15.IEC61968.AssetModels",
    "TransformerTankInfo": "CIM15.IEC61968.AssetModels",
    "PowerTransformerInfo": "CIM15.IEC61968.AssetModels",
    "OpenCircuitTest": "CIM15.IEC61968.AssetModels",
    "CableInfo": "CIM15.IEC61968.AssetModels",
    "TransformerEndInfo": "CIM15.IEC61968.AssetModels",
    "NoLoadTest": "CIM15.IEC61968.AssetModels",
    "OverheadConductorInfo": "CIM15.IEC61968.AssetModels",
    "ConcentricNeutralCableInfo": "CIM15.IEC61968.AssetModels",
    "WireArrangement": "CIM15.IEC61968.AssetModels",
    "TransformerTest": "CIM15.IEC61968.AssetModels",
    "SDPLocation": "CIM15.IEC61968.Metering",
    "Reading": "CIM15.IEC61968.Metering",
    "ServiceDeliveryPoint": "CIM15.IEC61968.Metering",
    "ElectricMeteringFunction": "CIM15.IEC61968.Metering",
    "DemandResponseProgram": "CIM15.IEC61968.Metering",
    "ReadingMultiplier": "CIM15.IEC61968.Metering",
    "MeterReading": "CIM15.IEC61968.Metering",
    "ReadingQuality": "CIM15.IEC61968.Metering",
    "EndDeviceEvent": "CIM15.IEC61968.Metering",
    "IntervalReading": "CIM15.IEC61968.Metering",
    "Meter": "CIM15.IEC61968.Metering",
    "MeterServiceWork": "CIM15.IEC61968.Metering",
    "PendingCalculation": "CIM15.IEC61968.Metering",
    "IntervalBlock": "CIM15.IEC61968.Metering",
    "EndDeviceFunction": "CIM15.IEC61968.Metering",
    "ComFunction": "CIM15.IEC61968.Metering",
    "EndDevice": "CIM15.IEC61968.Metering",
    "SimpleEndDeviceFunction": "CIM15.IEC61968.Metering",
    "EndDeviceGroup": "CIM15.IEC61968.Metering",
    "Register": "CIM15.IEC61968.Metering",
    "EndDeviceControl": "CIM15.IEC61968.Metering",
    "DynamicDemand": "CIM15.IEC61968.Metering",
    "ReadingType": "CIM15.IEC61968.Metering",
    "VendorShift": "CIM15.IEC61968.PaymentMetering",
    "Transactor": "CIM15.IEC61968.PaymentMetering",
    "CashierShift": "CIM15.IEC61968.PaymentMetering",
    "TariffProfile": "CIM15.IEC61968.PaymentMetering",
    "AccountingUnit": "CIM15.IEC61968.PaymentMetering",
    "Transaction": "CIM15.IEC61968.PaymentMetering",
    "TimeTariffInterval": "CIM15.IEC61968.PaymentMetering",
    "Charge": "CIM15.IEC61968.PaymentMetering",
    "AuxiliaryAgreement": "CIM15.IEC61968.PaymentMetering",
    "Tender": "CIM15.IEC61968.PaymentMetering",
    "ServiceSupplier": "CIM15.IEC61968.PaymentMetering",
    "MerchantAgreement": "CIM15.IEC61968.PaymentMetering",
    "LineDetail": "CIM15.IEC61968.PaymentMetering",
    "ConsumptionTariffInterval": "CIM15.IEC61968.PaymentMetering",
    "Vendor": "CIM15.IEC61968.PaymentMetering",
    "Cheque": "CIM15.IEC61968.PaymentMetering",
    "AccountMovement": "CIM15.IEC61968.PaymentMetering",
    "Shift": "CIM15.IEC61968.PaymentMetering",
    "Receipt": "CIM15.IEC61968.PaymentMetering",
    "Due": "CIM15.IEC61968.PaymentMetering",
    "BankAccountDetail": "CIM15.IEC61968.PaymentMetering",
    "AuxiliaryAccount": "CIM15.IEC61968.PaymentMetering",
    "Cashier": "CIM15.IEC61968.PaymentMetering",
    "Card": "CIM15.IEC61968.PaymentMetering",
    "MerchantAccount": "CIM15.IEC61968.PaymentMetering",
    "PointOfSale": "CIM15.IEC61968.PaymentMetering",
    "ProductAssetModel": "CIM15.IEC61968.Assets",
    "AssetModel": "CIM15.IEC61968.Assets",
    "Asset": "CIM15.IEC61968.Assets",
    "ComMedia": "CIM15.IEC61968.Assets",
    "AssetContainer": "CIM15.IEC61968.Assets",
    "AssetFunction": "CIM15.IEC61968.Assets",
    "Seal": "CIM15.IEC61968.Assets",
    "AssetInfo": "CIM15.IEC61968.Assets",
    "AcceptanceTest": "CIM15.IEC61968.Assets",
    "Work": "CIM15.IEC61968.Work",
    "Tariff": "CIM15.IEC61968.Customers",
    "CustomerAccount": "CIM15.IEC61968.Customers",
    "ServiceLocation": "CIM15.IEC61968.Customers",
    "CustomerAgreement": "CIM15.IEC61968.Customers",
    "ServiceCategory": "CIM15.IEC61968.Customers",
    "PricingStructure": "CIM15.IEC61968.Customers",
    "Customer": "CIM15.IEC61968.Customers",
    "ConnectDisconnectFunction": "CIM15.IEC61968.LoadControl",
    "RemoteConnectDisconnectInfo": "CIM15.IEC61968.LoadControl",
    "MarketParticipant": "CIM15.IEC62325",
    "IEC62325CIMVersion": "CIM15.IEC62325",
    "MarketRole": "CIM15.IEC62325",
    "PackageDependenciesCIMVeresion": "CIM15.PackageDependencies",
}


class CIMTime(str):
    pass

class CIMDateTime(str):
    pass

class CIMDuration(str):
    pass

class CIMGYear(str):
    pass

class CIMDate(str):
    pass

class CIMGMonthDay(str):
    pass

class CIMGMonth(str):
    pass

class CIMGDay(str):
    pass

class CIMGYearMonth(str):
    pass
