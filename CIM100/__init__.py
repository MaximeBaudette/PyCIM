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
# Modified by Gustav Holm (guholm@kth.se) & Francis J. Gomez (fragom@kth.se)
# Modified date: 05/06/2017

from CIM100.CombinedVersion import CombinedVersion
from CIM100.Element import Element
from CIM100.Stereotype import Stereotype
from CIM100.Package import Package

nsURI = "http://iec.ch/TC57/CIM100"
nsPrefix = "cim"

packageMap = {
    "CombinedVersion": "CIM100",
    "Element": "CIM100",
    "Stereotype": "CIM100",
    "Package": "CIM100",
    "IEC61970CIMVersion": "CIM100.IEC61970",
    "RemoteSource": "CIM100.IEC61970.Base.SCADA",
    "RemotePoint": "CIM100.IEC61970.Base.SCADA",
    "RemoteUnit": "CIM100.IEC61970.Base.SCADA",
    "RemoteControl": "CIM100.IEC61970.Base.SCADA",
    "CommunicationLink": "CIM100.IEC61970.Base.SCADA",
    "Reservoir": "CIM100.IEC61970.Base.Generation.Production",
    "CogenerationPlant": "CIM100.IEC61970.Base.Generation.Production",
    "GenUnitOpSchedule": "CIM100.IEC61970.Base.Generation.Production",
    "FuelAllocationSchedule": "CIM100.IEC61970.Base.Generation.Production",
    "GrossToNetActivePowerCurve": "CIM100.IEC61970.Base.Generation.Production",
    "LevelVsVolumeCurve": "CIM100.IEC61970.Base.Generation.Production",
    "StartRampCurve": "CIM100.IEC61970.Base.Generation.Production",
    "NuclearGeneratingUnit": "CIM100.IEC61970.Base.Generation.Production",
    "EmissionCurve": "CIM100.IEC61970.Base.Generation.Production",
    "HydroPumpOpSchedule": "CIM100.IEC61970.Base.Generation.Production",
    "SteamSendoutSchedule": "CIM100.IEC61970.Base.Generation.Production",
    "TargetLevelSchedule": "CIM100.IEC61970.Base.Generation.Production",
    "CombinedCyclePlant": "CIM100.IEC61970.Base.Generation.Production",
    "HeatRateCurve": "CIM100.IEC61970.Base.Generation.Production",
    "ThermalGeneratingUnit": "CIM100.IEC61970.Base.Generation.Production",
    "EmissionAccount": "CIM100.IEC61970.Base.Generation.Production",
    "PenstockLossCurve": "CIM100.IEC61970.Base.Generation.Production",
    "StartupModel": "CIM100.IEC61970.Base.Generation.Production",
    "HydroGeneratingUnit": "CIM100.IEC61970.Base.Generation.Production",
    "GenUnitOpCostCurve": "CIM100.IEC61970.Base.Generation.Production",
    "IncrementalHeatRateCurve": "CIM100.IEC61970.Base.Generation.Production",
    "FossilFuel": "CIM100.IEC61970.Base.Generation.Production",
    "GeneratingUnit": "CIM100.IEC61970.Base.Generation.Production",
    "StartIgnFuelCurve": "CIM100.IEC61970.Base.Generation.Production",
    "StartMainFuelCurve": "CIM100.IEC61970.Base.Generation.Production",
    "TailbayLossCurve": "CIM100.IEC61970.Base.Generation.Production",
    "HydroPump": "CIM100.IEC61970.Base.Generation.Production",
    "InflowForecast": "CIM100.IEC61970.Base.Generation.Production",
    "HydroGeneratingEfficiencyCurve": "CIM100.IEC61970.Base.Generation.Production",
    "ShutdownCurve": "CIM100.IEC61970.Base.Generation.Production",
    "HydroPowerPlant": "CIM100.IEC61970.Base.Generation.Production",
    "CAESPlant": "CIM100.IEC61970.Base.Generation.Production",
    "AirCompressor": "CIM100.IEC61970.Base.Generation.Production",
    "HeatInputCurve": "CIM100.IEC61970.Base.Generation.Production",
    "WindGeneratingUnit": "CIM100.IEC61970.Base.Generation.Production",
    "BWRSteamSupply": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "HydroTurbine": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "SteamTurbine": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "SteamSupply": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "FossilSteamSupply": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "Subcritical": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "PWRSteamSupply": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "PrimeMover": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "CombustionTurbine": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "HeatRecoveryBoiler": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "Supercritical": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "DrumBoiler": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "CTTempActivePowerCurve": "CIM100.IEC61970.Base.Generation.GenerationDynamics",
    "EquipmentItem": "CIM100.IEC61970.Informative.InfWork",
    "Appointment": "CIM100.IEC61970.Informative.InfWork",
    "WorkStatusEntry": "CIM100.IEC61970.Informative.InfWork",
    "BusinessCase": "CIM100.IEC61970.Informative.InfWork",
    "TypeMaterial": "CIM100.IEC61970.Informative.InfWork",
    "DesignLocation": "CIM100.IEC61970.Informative.InfWork",
    "OverheadCost": "CIM100.IEC61970.Informative.InfWork",
    "Crew": "CIM100.IEC61970.Informative.InfWork",
    "DiagnosisDataSet": "CIM100.IEC61970.Informative.InfWork",
    "CUAsset": "CIM100.IEC61970.Informative.InfWork",
    "Request": "CIM100.IEC61970.Informative.InfWork",
    "Design": "CIM100.IEC61970.Informative.InfWork",
    "WorkTask": "CIM100.IEC61970.Informative.InfWork",
    "ConditionFactor": "CIM100.IEC61970.Informative.InfWork",
    "QualificationRequirement": "CIM100.IEC61970.Informative.InfWork",
    "WorkLocation": "CIM100.IEC61970.Informative.InfWork",
    "CostType": "CIM100.IEC61970.Informative.InfWork",
    "CUMaterialItem": "CIM100.IEC61970.Informative.InfWork",
    "PropertyUnit": "CIM100.IEC61970.Informative.InfWork",
    "Project": "CIM100.IEC61970.Informative.InfWork",
    "CULaborItem": "CIM100.IEC61970.Informative.InfWork",
    "LaborItem": "CIM100.IEC61970.Informative.InfWork",
    "WorkFlowStep": "CIM100.IEC61970.Informative.InfWork",
    "InspectionDataSet": "CIM100.IEC61970.Informative.InfWork",
    "WorkCostDetail": "CIM100.IEC61970.Informative.InfWork",
    "CompatibleUnit": "CIM100.IEC61970.Informative.InfWork",
    "WorkCostSummary": "CIM100.IEC61970.Informative.InfWork",
    "NonStandardItem": "CIM100.IEC61970.Informative.InfWork",
    "InfoQuestion": "CIM100.IEC61970.Informative.InfWork",
    "Regulation": "CIM100.IEC61970.Informative.InfWork",
    "ContractorItem": "CIM100.IEC61970.Informative.InfWork",
    "CUAllowableAction": "CIM100.IEC61970.Informative.InfWork",
    "CULaborCode": "CIM100.IEC61970.Informative.InfWork",
    "AccessPermit": "CIM100.IEC61970.Informative.InfWork",
    "CUWorkEquipmentItem": "CIM100.IEC61970.Informative.InfWork",
    "DesignLocationCU": "CIM100.IEC61970.Informative.InfWork",
    "MaintenanceDataSet": "CIM100.IEC61970.Informative.InfWork",
    "MiscCostItem": "CIM100.IEC61970.Informative.InfWork",
    "MaterialItem": "CIM100.IEC61970.Informative.InfWork",
    "ShiftPattern": "CIM100.IEC61970.Informative.InfWork",
    "Capability": "CIM100.IEC61970.Informative.InfWork",
    "Usage": "CIM100.IEC61970.Informative.InfWork",
    "OneCallRequest": "CIM100.IEC61970.Informative.InfWork",
    "Assignment": "CIM100.IEC61970.Informative.InfWork",
    "CUContractorItem": "CIM100.IEC61970.Informative.InfWork",
    "CUGroup": "CIM100.IEC61970.Informative.InfWork",
    "ErpRecDelvLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpLedgerBudget": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpTimeEntry": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpCompetency": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPurchaseOrder": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpEngChangeOrder": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpProjectAccounting": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpRecLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPayableLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpLedBudLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpRequisition": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpOrganisation": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpInvoice": "CIM100.IEC61970.Informative.InfERPSupport",
    "DocErpPersonRole": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpBankAccount": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpQuote": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPerson": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpItemMaster": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpBOM": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpInventoryCount": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpIssueInventory": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPayable": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpLedger": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPOLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpLedgerEntry": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPayment": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpReceivable": "CIM100.IEC61970.Informative.InfERPSupport",
    "DocOrgRole": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpReqLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpTimeSheet": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpInventory": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpChartOfAccounts": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpSiteLevelData": "CIM100.IEC61970.Informative.InfERPSupport",
    "OrgErpPersonRole": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpReceiveDelivery": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpSalesOrder": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpJournalEntry": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpInvoiceLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "OrgOrgRole": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpJournal": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpPersonnel": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpQuoteLineItem": "CIM100.IEC61970.Informative.InfERPSupport",
    "ErpBomItemData": "CIM100.IEC61970.Informative.InfERPSupport",
    "Role": "CIM100.IEC61970.Informative.InfCommon",
    "Bank": "CIM100.IEC61970.Informative.InfCommon",
    "Skill": "CIM100.IEC61970.Informative.InfCommon",
    "BusinessRole": "CIM100.IEC61970.Informative.InfCommon",
    "ScheduledEvent": "CIM100.IEC61970.Informative.InfCommon",
    "ScheduleParameterInfo": "CIM100.IEC61970.Informative.InfCommon",
    "DocPsrRole": "CIM100.IEC61970.Informative.InfCommon",
    "Ratio": "CIM100.IEC61970.Informative.InfCommon",
    "BankAccount": "CIM100.IEC61970.Informative.InfCommon",
    "Craft": "CIM100.IEC61970.Informative.InfCommon",
    "DocDocRole": "CIM100.IEC61970.Informative.InfCommon",
    "BusinessPlan": "CIM100.IEC61970.Informative.InfCommon",
    "FACTSDevice": "CIM100.IEC61970.Informative.InfAssets",
    "DocAssetRole": "CIM100.IEC61970.Informative.InfAssets",
    "DuctBank": "CIM100.IEC61970.Informative.InfAssets",
    "ConductorAsset": "CIM100.IEC61970.Informative.InfAssets",
    "FinancialInfo": "CIM100.IEC61970.Informative.InfAssets",
    "ProtectionEquipmentInfo": "CIM100.IEC61970.Informative.InfAssets",
    "ProcedureDataSet": "CIM100.IEC61970.Informative.InfAssets",
    "WindingInsulation": "CIM100.IEC61970.Informative.InfAssets",
    "Specification": "CIM100.IEC61970.Informative.InfAssets",
    "UndergroundStructure": "CIM100.IEC61970.Informative.InfAssets",
    "PotentialTransformerInfo": "CIM100.IEC61970.Informative.InfAssets",
    "Structure": "CIM100.IEC61970.Informative.InfAssets",
    "CurrentTransformerInfo": "CIM100.IEC61970.Informative.InfAssets",
    "BushingInsulationPF": "CIM100.IEC61970.Informative.InfAssets",
    "Joint": "CIM100.IEC61970.Informative.InfAssets",
    "ElectricalInfo": "CIM100.IEC61970.Informative.InfAssets",
    "WorkEquipment": "CIM100.IEC61970.Informative.InfAssets",
    "FaultIndicatorInfo": "CIM100.IEC61970.Informative.InfAssets",
    "Duct": "CIM100.IEC61970.Informative.InfAssets",
    "PowerRating": "CIM100.IEC61970.Informative.InfAssets",
    "AssetAssetRole": "CIM100.IEC61970.Informative.InfAssets",
    "TransformerAsset": "CIM100.IEC61970.Informative.InfAssets",
    "Procedure": "CIM100.IEC61970.Informative.InfAssets",
    "BreakerInfo": "CIM100.IEC61970.Informative.InfAssets",
    "CompositeSwitchInfo": "CIM100.IEC61970.Informative.InfAssets",
    "Cabinet": "CIM100.IEC61970.Informative.InfAssets",
    "Bushing": "CIM100.IEC61970.Informative.InfAssets",
    "Vehicle": "CIM100.IEC61970.Informative.InfAssets",
    "SurgeProtectorInfo": "CIM100.IEC61970.Informative.InfAssets",
    "StructureSupport": "CIM100.IEC61970.Informative.InfAssets",
    "ComEquipment": "CIM100.IEC61970.Informative.InfAssets",
    "AssetPropertyCurve": "CIM100.IEC61970.Informative.InfAssets",
    "FailureEvent": "CIM100.IEC61970.Informative.InfAssets",
    "DimensionsInfo": "CIM100.IEC61970.Informative.InfAssets",
    "Tower": "CIM100.IEC61970.Informative.InfAssets",
    "MountingConnection": "CIM100.IEC61970.Informative.InfAssets",
    "Medium": "CIM100.IEC61970.Informative.InfAssets",
    "RecloserInfo": "CIM100.IEC61970.Informative.InfAssets",
    "Facility": "CIM100.IEC61970.Informative.InfAssets",
    "ShuntImpedanceInfo": "CIM100.IEC61970.Informative.InfAssets",
    "ShuntCompensatorInfo": "CIM100.IEC61970.Informative.InfAssets",
    "MountingPoint": "CIM100.IEC61970.Informative.InfAssets",
    "SubstationAsset": "CIM100.IEC61970.Informative.InfAssets",
    "Streetlight": "CIM100.IEC61970.Informative.InfAssets",
    "Tool": "CIM100.IEC61970.Informative.InfAssets",
    "SVC": "CIM100.IEC61970.Informative.InfAssets",
    "OrgAssetRole": "CIM100.IEC61970.Informative.InfAssets",
    "TestDataSet": "CIM100.IEC61970.Informative.InfAssets",
    "GenericAssetModelOrMaterial": "CIM100.IEC61970.Informative.InfAssets",
    "ReliabilityInfo": "CIM100.IEC61970.Informative.InfAssets",
    "TransformerObservation": "CIM100.IEC61970.Informative.InfAssets",
    "Pole": "CIM100.IEC61970.Informative.InfAssets",
    "SwitchInfo": "CIM100.IEC61970.Informative.InfAssets",
    "StandardIndustryCode": "CIM100.IEC61970.Informative.InfCustomers",
    "OutageHistory": "CIM100.IEC61970.Informative.InfCustomers",
    "ComplianceEvent": "CIM100.IEC61970.Informative.InfCustomers",
    "CustomerBillingInfo": "CIM100.IEC61970.Informative.InfCustomers",
    "ServiceGuarantee": "CIM100.IEC61970.Informative.InfCustomers",
    "SubscribePowerCurve": "CIM100.IEC61970.Informative.InfCustomers",
    "ExternalCustomerAgreement": "CIM100.IEC61970.Informative.InfCustomers",
    "PowerQualityPricing": "CIM100.IEC61970.Informative.InfCustomers",
    "WorkBillingInfo": "CIM100.IEC61970.Informative.InfCustomers",
    "OutageRecord": "CIM100.IEC61970.Informative.InfOperations",
    "OutageReport": "CIM100.IEC61970.Informative.InfOperations",
    "ChangeItem": "CIM100.IEC61970.Informative.InfOperations",
    "PSREvent": "CIM100.IEC61970.Informative.InfOperations",
    "PlannedOutage": "CIM100.IEC61970.Informative.InfOperations",
    "CircuitSection": "CIM100.IEC61970.Informative.InfOperations",
    "SafetyDocument": "CIM100.IEC61970.Informative.InfOperations",
    "OperationalRestriction": "CIM100.IEC61970.Informative.InfOperations",
    "ChangeSet": "CIM100.IEC61970.Informative.InfOperations",
    "SwitchingSchedule": "CIM100.IEC61970.Informative.InfOperations",
    "Circuit": "CIM100.IEC61970.Informative.InfOperations",
    "NetworkDataSet": "CIM100.IEC61970.Informative.InfOperations",
    "OutageStep": "CIM100.IEC61970.Informative.InfOperations",
    "OrgPsrRole": "CIM100.IEC61970.Informative.InfOperations",
    "OutageCode": "CIM100.IEC61970.Informative.InfOperations",
    "IncidentCode": "CIM100.IEC61970.Informative.InfOperations",
    "LandBase": "CIM100.IEC61970.Informative.InfOperations",
    "ErpPersonScheduleStepRole": "CIM100.IEC61970.Informative.InfOperations",
    "SwitchingStep": "CIM100.IEC61970.Informative.InfOperations",
    "CallBack": "CIM100.IEC61970.Informative.InfOperations",
    "TroubleTicket": "CIM100.IEC61970.Informative.InfOperations",
    "IncidentRecord": "CIM100.IEC61970.Informative.InfOperations",
    "OutageNotification": "CIM100.IEC61970.Informative.InfOperations",
    "OutageStepPsrRole": "CIM100.IEC61970.Informative.InfOperations",
    "LocationGrant": "CIM100.IEC61970.Informative.InfLocations",
    "RightOfWay": "CIM100.IEC61970.Informative.InfLocations",
    "PersonPropertyRole": "CIM100.IEC61970.Informative.InfLocations",
    "Zone": "CIM100.IEC61970.Informative.InfLocations",
    "RedLine": "CIM100.IEC61970.Informative.InfLocations",
    "Route": "CIM100.IEC61970.Informative.InfLocations",
    "OrgPropertyRole": "CIM100.IEC61970.Informative.InfLocations",
    "Direction": "CIM100.IEC61970.Informative.InfLocations",
    "LandProperty": "CIM100.IEC61970.Informative.InfLocations",
    "Hazard": "CIM100.IEC61970.Informative.InfLocations",
    "GmlFeatureType": "CIM100.IEC61970.Informative.InfGMLSupport",
    "Map": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlPointGeometry": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlHalo": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlColour": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlFont": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlPolygonSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlStroke": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlBaseSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlPosition": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlTextSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlPolygonGeometry": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlObservation": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlMark": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlGraphic": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlLabelPlacement": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlGeometryStyle": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlLineGeometry": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlValue": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlLineSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlDiagramObject": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlPointSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlTopologyStyle": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlSelector": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlSvgParameter": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlLabelStyle": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlFill": "CIM100.IEC61970.Informative.InfGMLSupport",
    "Diagram": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlFeatureStyle": "CIM100.IEC61970.Informative.InfGMLSupport",
    "GmlRasterSymbol": "CIM100.IEC61970.Informative.InfGMLSupport",
    "ModelingAuthority": "CIM100.IEC61970.Informative.InfCore",
    "ModelingAuthoritySet": "CIM100.IEC61970.Informative.InfCore",
    "LoadMgmtRecord": "CIM100.IEC61970.Informative.InfLoadControl",
    "LoadShedFunction": "CIM100.IEC61970.Informative.InfLoadControl",
    "LoadMgmtFunction": "CIM100.IEC61970.Informative.InfLoadControl",
    "LoadLimitFunction": "CIM100.IEC61970.Informative.InfLoadControl",
    "GasMeteringFunction": "CIM100.IEC61970.Informative.InfMetering",
    "WaterMeteringFunction": "CIM100.IEC61970.Informative.InfMetering",
    "AssetModelCatalogue": "CIM100.IEC61970.Informative.InfAssetModels",
    "TransformerAssetModel": "CIM100.IEC61970.Informative.InfAssetModels",
    "AssetModelCatalogueItem": "CIM100.IEC61970.Informative.InfAssetModels",
    "TypeAssetCatalogue": "CIM100.IEC61970.Informative.InfTypeAsset",
    "GeneratorTypeAsset": "CIM100.IEC61970.Informative.InfTypeAsset",
    "SvVoltage": "CIM100.IEC61970.Base.StateVariables",
    "SvShortCircuit": "CIM100.IEC61970.Base.StateVariables",
    "SvShuntCompensatorSections": "CIM100.IEC61970.Base.StateVariables",
    "StateVariable": "CIM100.IEC61970.Base.StateVariables",
    "SvTapStep": "CIM100.IEC61970.Base.StateVariables",
    "SvStatus": "CIM100.IEC61970.Base.StateVariables",
    "SvInjection": "CIM100.IEC61970.Base.StateVariables",
    "SvPowerFlow": "CIM100.IEC61970.Base.StateVariables",
    "TopologicalIsland": "CIM100.IEC61970.Base.StateVariables",
    "PhaseImpedanceData": "CIM100.IEC61970.Base.Wires",
    "TapSchedule": "CIM100.IEC61970.Base.Wires",
    "TransformerStarImpedance": "CIM100.IEC61970.Base.Wires",
    "Recloser": "CIM100.IEC61970.Base.Wires",
    "RatioTapChangerTabularPoint": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChangerTabular": "CIM100.IEC61970.Base.Wires",
    "RatioTapChanger": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChangerLinear": "CIM100.IEC61970.Base.Wires",
    "ACLineSegment": "CIM100.IEC61970.Base.Wires",
    "ACLineSegmentPhase": "CIM100.IEC61970.Base.WiresPhaseModel",
    "PowerTransformerEnd": "CIM100.IEC61970.Base.Wires",
    "Junction": "CIM100.IEC61970.Base.Wires",
    "RegulatingCondEq": "CIM100.IEC61970.Base.Wires",
    "Sectionaliser": "CIM100.IEC61970.Base.Wires",
    "RatioTapChangerTabular": "CIM100.IEC61970.Base.Wires",
    "PowerTransformer": "CIM100.IEC61970.Base.Wires",
    "Fuse": "CIM100.IEC61970.Base.Wires",
    "EnergyConsumer": "CIM100.IEC61970.Base.Wires",
    "Disconnector": "CIM100.IEC61970.Base.Wires",
    "Connector": "CIM100.IEC61970.Base.Wires",
    "ReactiveCapabilityCurve": "CIM100.IEC61970.Base.Wires",
    "Plant": "CIM100.IEC61970.Base.Wires",
    "GroundDisconnector": "CIM100.IEC61970.Base.Wires",
    "Resistor": "CIM100.IEC61970.Base.Wires",
    "SynchronousMachine": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChangerAsymetrical": "CIM100.IEC61970.Base.Wires",
    "RectifierInverter": "CIM100.IEC61970.Base.Wires",
    "SeriesCompensator": "CIM100.IEC61970.Base.Wires",
    "TapChangerControl": "CIM100.IEC61970.Base.Wires",
    "RegulatingControl": "CIM100.IEC61970.Base.Wires",
    "ProtectedSwitch": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChanger": "CIM100.IEC61970.Base.Wires",
    "Ground": "CIM100.IEC61970.Base.Wires",
    "CompositeSwitch": "CIM100.IEC61970.Base.Wires",
    "RegulationSchedule": "CIM100.IEC61970.Base.Wires",
    "TransformerTankEnd": "CIM100.IEC61970.Base.Wires",
    "Breaker": "CIM100.IEC61970.Base.Wires",
    "MutualCoupling": "CIM100.IEC61970.Base.Wires",
    "Line": "CIM100.IEC61970.Base.Wires",
    "PerLengthPhaseImpedance": "CIM100.IEC61970.Base.Wires",
    "FrequencyConverter": "CIM100.IEC61970.Base.Wires",
    "ShuntCompensator": "CIM100.IEC61970.Base.Wires",
    "VoltageControlZone": "CIM100.IEC61970.Base.Wires",
    "LoadBreakSwitch": "CIM100.IEC61970.Base.Wires",
    "BusbarSection": "CIM100.IEC61970.Base.Wires",
    "TransformerEnd": "CIM100.IEC61970.Base.Wires",
    "TransformerCoreAdmittance": "CIM100.IEC61970.Base.Wires",
    "StaticVarCompensator": "CIM100.IEC61970.Base.Wires",
    "Switch": "CIM100.IEC61970.Base.Wires",
    "PerLengthSequenceImpedance": "CIM100.IEC61970.Base.Wires",
    "TransformerMeshImpedance": "CIM100.IEC61970.Base.Wires",
    "SwitchSchedule": "CIM100.IEC61970.Base.Wires",
    "EnergySource": "CIM100.IEC61970.Base.Wires",
    "TransformerTank": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChangerTabularPoint": "CIM100.IEC61970.Base.Wires",
    "DCLineSegment": "CIM100.IEC61970.Base.Wires",
    "TapChanger": "CIM100.IEC61970.Base.Wires",
    "Conductor": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChangerNonLinear": "CIM100.IEC61970.Base.Wires",
    "PhaseTapChangerSymetrical": "CIM100.IEC61970.Base.Wires",
    "Jumper": "CIM100.IEC61970.Base.Wires",
    "PowerElectronicsConnection": "CIM100.IEC61970.Base.Wires",
    "PowerElectronicsConnectionPhase": "CIM100.IEC61970.Base.Wires",
    "AccumulatorLimit": "CIM100.IEC61970.Base.Meas",
    "ValueToAlias": "CIM100.IEC61970.Base.Meas",
    "MeasurementValueSource": "CIM100.IEC61970.Base.Meas",
    "Analog": "CIM100.IEC61970.Base.Meas",
    "AnalogValue": "CIM100.IEC61970.Base.Meas",
    "Measurement": "CIM100.IEC61970.Base.Meas",
    "ControlType": "CIM100.IEC61970.Base.Meas",
    "StringMeasurementValue": "CIM100.IEC61970.Base.Meas",
    "StringMeasurement": "CIM100.IEC61970.Base.Meas",
    "AnalogLimit": "CIM100.IEC61970.Base.Meas",
    "SetPoint": "CIM100.IEC61970.Base.Meas",
    "Limit": "CIM100.IEC61970.Base.Meas",
    "Discrete": "CIM100.IEC61970.Base.Meas",
    "ValueAliasSet": "CIM100.IEC61970.Base.Meas",
    "Quality61850": "CIM100.IEC61970.Base.Meas",
    "AccumulatorValue": "CIM100.IEC61970.Base.Meas",
    "Command": "CIM100.IEC61970.Base.Meas",
    "Accumulator": "CIM100.IEC61970.Base.Meas",
    "MeasurementValueQuality": "CIM100.IEC61970.Base.Meas",
    "MeasurementValue": "CIM100.IEC61970.Base.Meas",
    "DiscreteValue": "CIM100.IEC61970.Base.Meas",
    "AnalogLimitSet": "CIM100.IEC61970.Base.Meas",
    "LimitSet": "CIM100.IEC61970.Base.Meas",
    "AccumulatorLimitSet": "CIM100.IEC61970.Base.Meas",
    "Control": "CIM100.IEC61970.Base.Meas",
    "ConformLoad": "CIM100.IEC61970.Base.LoadModel",
    "ConformLoadGroup": "CIM100.IEC61970.Base.LoadModel",
    "SeasonDayTypeSchedule": "CIM100.IEC61970.Base.LoadModel",
    "LoadGroup": "CIM100.IEC61970.Base.LoadModel",
    "ConformLoadSchedule": "CIM100.IEC61970.Base.LoadModel",
    "LoadArea": "CIM100.IEC61970.Base.LoadModel",
    "PowerCutZone": "CIM100.IEC61970.Base.LoadModel",
    "LoadResponseCharacteristic": "CIM100.IEC61970.Base.LoadModel",
    "NonConformLoad": "CIM100.IEC61970.Base.LoadModel",
    "StationSupply": "CIM100.IEC61970.Base.LoadModel",
    "EnergyArea": "CIM100.IEC61970.Base.LoadModel",
    "NonConformLoadSchedule": "CIM100.IEC61970.Base.LoadModel",
    "NonConformLoadGroup": "CIM100.IEC61970.Base.LoadModel",
    "DayType": "CIM100.IEC61970.Base.LoadModel",
    "SubLoadArea": "CIM100.IEC61970.Base.LoadModel",
    "Season": "CIM100.IEC61970.Base.LoadModel",
    "SwitchPhase": "CIM100.IEC61970.Base.WiresPhaseModel",
    "ShuntCompensatorPhase": "CIM100.IEC61970.Base.WiresPhaseModel",
    "EnergyConsumerPhase": "CIM100.IEC61970.Base.WiresPhaseModel",
    "AltTieMeas": "CIM100.IEC61970.Base.ControlArea",
    "AltGeneratingUnitMeas": "CIM100.IEC61970.Base.ControlArea",
    "TieFlow": "CIM100.IEC61970.Base.ControlArea",
    "ControlArea": "CIM100.IEC61970.Base.ControlArea",
    "ControlAreaGeneratingUnit": "CIM100.IEC61970.Base.ControlArea",
    "PotentialTransformer": "CIM100.IEC61970.Base.AuxiliaryEquipment",
    "Sensor": "CIM100.IEC61970.Base.AuxiliaryEquipment",
    "AuxiliaryEquipment": "CIM100.IEC61970.Base.AuxiliaryEquipment",
    "CurrentTransformer": "CIM100.IEC61970.Base.AuxiliaryEquipment",
    "SurgeProtector": "CIM100.IEC61970.Base.AuxiliaryEquipment",
    "FaultIndicator": "CIM100.IEC61970.Base.AuxiliaryEquipment",
    "DateTimeInterval": "CIM100.IEC61970.Base.Domain",
    "PowerSystemResource": "CIM100.IEC61970.Base.Core",
    "NameTypeAuthority": "CIM100.IEC61970.Base.Core",
    "Equipment": "CIM100.IEC61970.Base.Core",
    "ConductingEquipment": "CIM100.IEC61970.Base.Core",
    "RegularTimePoint": "CIM100.IEC61970.Base.Core",
    "ConnectivityNode": "CIM100.IEC61970.Base.Core",
    "PSRType": "CIM100.IEC61970.Base.Core",
    "ConnectivityNodeContainer": "CIM100.IEC61970.Base.Core",
    "Bay": "CIM100.IEC61970.Base.Core",
    "EquipmentContainer": "CIM100.IEC61970.Base.Core",
    "ReportingGroup": "CIM100.IEC61970.Base.Core",
    "BasePower": "CIM100.IEC61970.Base.Core",
    "PsrList": "CIM100.IEC61970.Base.Core",
    "IdentifiedObject": "CIM100.IEC61970.Base.Core",
    "BasicIntervalSchedule": "CIM100.IEC61970.Base.Core",
    "Curve": "CIM100.IEC61970.Base.Core",
    "GeographicalRegion": "CIM100.IEC61970.Base.Core",
    "CurveData": "CIM100.IEC61970.Base.Core",
    "SubGeographicalRegion": "CIM100.IEC61970.Base.Core",
    "NameType": "CIM100.IEC61970.Base.Core",
    "Substation": "CIM100.IEC61970.Base.Core",
    "Feeder": "CIM100.IEC61970.Base.Core",
    "Name": "CIM100.IEC61970.Base.Core",
    "BaseVoltage": "CIM100.IEC61970.Base.Core",
    "Terminal": "CIM100.IEC61970.Base.Core",
    "IrregularIntervalSchedule": "CIM100.IEC61970.Base.Core",
    "RegularIntervalSchedule": "CIM100.IEC61970.Base.Core",
    "OperatingParticipant": "CIM100.IEC61970.Base.Core",
    "OperatingShare": "CIM100.IEC61970.Base.Core",
    "VoltageLevel": "CIM100.IEC61970.Base.Core",
    "ReportingSuperGroup": "CIM100.IEC61970.Base.Core",
    "IrregularTimePoint": "CIM100.IEC61970.Base.Core",
    "TextDiagramObject": "CIM100.IEC61970.Graphics",
    "DiagramObjectGluePoint": "CIM100.IEC61970.Graphics",
    "DiagramObject": "CIM100.IEC61970.Graphics",
    "DiagramObjectStyle": "CIM100.IEC61970.Graphics",
    "DiagramObjectPoint": "CIM100.IEC61970.Graphics",
    "VisibilityLayer": "CIM100.IEC61970.Graphics",
    "ApparentPowerLimit": "CIM100.IEC61970.Base.OperationalLimits",
    "ActivePowerLimit": "CIM100.IEC61970.Base.OperationalLimits",
    "OperationalLimitType": "CIM100.IEC61970.Base.OperationalLimits",
    "BranchGroup": "CIM100.IEC61970.Base.OperationalLimits",
    "OperationalLimitSet": "CIM100.IEC61970.Base.OperationalLimits",
    "ActivePowerLimitSet": "CIM100.IEC61970.Base.OperationalLimits",
    "CurrentLimit": "CIM100.IEC61970.Base.OperationalLimits",
    "CurrentLimitSet": "CIM100.IEC61970.Base.OperationalLimits",
    "ApparentPowerLimitSet": "CIM100.IEC61970.Base.OperationalLimits",
    "BranchGroupTerminal": "CIM100.IEC61970.Base.OperationalLimits",
    "VoltageLimitSet": "CIM100.IEC61970.Base.OperationalLimits",
    "VoltageLimit": "CIM100.IEC61970.Base.OperationalLimits",
    "OperationalLimit": "CIM100.IEC61970.Base.OperationalLimits",
    "SwitchingOperation": "CIM100.IEC61970.Outage",
    "OutageSchedule": "CIM100.IEC61970.Outage",
    "ClearanceTagType": "CIM100.IEC61970.Outage",
    "ClearanceTag": "CIM100.IEC61970.Outage",
    "Cut": "CIM100.IEC61970.CutsJumpers",
    "Clamp": "CIM100.IEC61970.CutsJumpers",
    "RecloseSequence": "CIM100.IEC61970.Base.Protection",
    "SynchrocheckRelay": "CIM100.IEC61970.Base.Protection",
    "CurrentRelay": "CIM100.IEC61970.Base.Protection",
    "ProtectionEquipment": "CIM100.IEC61970.Base.Protection",
    "EquivalentShunt": "CIM100.IEC61970.Base.Equivalents",
    "EquivalentEquipment": "CIM100.IEC61970.Base.Equivalents",
    "EquivalentNetwork": "CIM100.IEC61970.Base.Equivalents",
    "EquivalentInjection": "CIM100.IEC61970.Base.Equivalents",
    "EquivalentBranch": "CIM100.IEC61970.Base.Equivalents",
    "ContingencyEquipment": "CIM100.IEC61970.Base.Contingency",
    "Contingency": "CIM100.IEC61970.Base.Contingency",
    "ContingencyElement": "CIM100.IEC61970.Base.Contingency",
    "BusNameMarker": "CIM100.IEC61970.Base.Topology",
    "TopologicalNode": "CIM100.IEC61970.Base.Topology",
    "IEC61968CIMVersion": "CIM100.IEC61968",
    "PostalAddress": "CIM100.IEC61968.Common",
    "Status": "CIM100.IEC61968.Common",
    "ElectronicAddress": "CIM100.IEC61968.Common",
    "Location": "CIM100.IEC61968.Common",
    "TownDetail": "CIM100.IEC61968.Common",
    "CoordinateSystem": "CIM100.IEC61968.Common",
    "Document": "CIM100.IEC61968.Common",
    "PositionPoint": "CIM100.IEC61968.Common",
    "UserAttribute": "CIM100.IEC61968.Common",
    "StreetAddress": "CIM100.IEC61968.Common",
    "StreetDetail": "CIM100.IEC61968.Common",
    "TimeSchedule": "CIM100.IEC61968.Common",
    "ActivityRecord": "CIM100.IEC61968.Common",
    "TimePoint": "CIM100.IEC61968.Common",
    "Organisation": "CIM100.IEC61968.Common",
    "TelephoneNumber": "CIM100.IEC61968.Common",
    "Agreement": "CIM100.IEC61968.Common",
    "ShortCircuitTest": "CIM100.IEC61968.AssetModels",
    "EndDeviceInfo": "CIM100.IEC61968.AssetModels",
    "WireType": "CIM100.IEC61968.AssetModels",
    "TapeShieldCableInfo": "CIM100.IEC61968.AssetModels",
    "ConductorInfo": "CIM100.IEC61968.AssetModels",
    "TapChangerInfo": "CIM100.IEC61968.AssetModels",
    "TransformerTankInfo": "CIM100.IEC61968.AssetModels",
    "PowerTransformerInfo": "CIM100.IEC61968.AssetModels",
    "OpenCircuitTest": "CIM100.IEC61968.AssetModels",
    "CableInfo": "CIM100.IEC61968.AssetModels",
    "TransformerEndInfo": "CIM100.IEC61968.AssetModels",
    "NoLoadTest": "CIM100.IEC61968.AssetModels",
    "OverheadConductorInfo": "CIM100.IEC61968.AssetModels",
    "ConcentricNeutralCableInfo": "CIM100.IEC61968.AssetModels",
    "WireArrangement": "CIM100.IEC61968.AssetModels",
    "TransformerTest": "CIM100.IEC61968.AssetModels",
    "SDPLocation": "CIM100.IEC61968.Metering",
    "Reading": "CIM100.IEC61968.Metering",
    "ServiceDeliveryPoint": "CIM100.IEC61968.Metering",
    "ElectricMeteringFunction": "CIM100.IEC61968.Metering",
    "DemandResponseProgram": "CIM100.IEC61968.Metering",
    "ReadingMultiplier": "CIM100.IEC61968.Metering",
    "MeterReading": "CIM100.IEC61968.Metering",
    "ReadingQuality": "CIM100.IEC61968.Metering",
    "EndDeviceEvent": "CIM100.IEC61968.Metering",
    "IntervalReading": "CIM100.IEC61968.Metering",
    "Meter": "CIM100.IEC61968.Metering",
    "MeterServiceWork": "CIM100.IEC61968.Metering",
    "PendingCalculation": "CIM100.IEC61968.Metering",
    "IntervalBlock": "CIM100.IEC61968.Metering",
    "EndDeviceFunction": "CIM100.IEC61968.Metering",
    "ComFunction": "CIM100.IEC61968.Metering",
    "EndDevice": "CIM100.IEC61968.Metering",
    "SimpleEndDeviceFunction": "CIM100.IEC61968.Metering",
    "EndDeviceGroup": "CIM100.IEC61968.Metering",
    "Register": "CIM100.IEC61968.Metering",
    "EndDeviceControl": "CIM100.IEC61968.Metering",
    "DynamicDemand": "CIM100.IEC61968.Metering",
    "ReadingType": "CIM100.IEC61968.Metering",
    "VendorShift": "CIM100.IEC61968.PaymentMetering",
    "Transactor": "CIM100.IEC61968.PaymentMetering",
    "CashierShift": "CIM100.IEC61968.PaymentMetering",
    "TariffProfile": "CIM100.IEC61968.PaymentMetering",
    "AccountingUnit": "CIM100.IEC61968.PaymentMetering",
    "Transaction": "CIM100.IEC61968.PaymentMetering",
    "TimeTariffInterval": "CIM100.IEC61968.PaymentMetering",
    "Charge": "CIM100.IEC61968.PaymentMetering",
    "AuxiliaryAgreement": "CIM100.IEC61968.PaymentMetering",
    "Tender": "CIM100.IEC61968.PaymentMetering",
    "ServiceSupplier": "CIM100.IEC61968.PaymentMetering",
    "MerchantAgreement": "CIM100.IEC61968.PaymentMetering",
    "LineDetail": "CIM100.IEC61968.PaymentMetering",
    "ConsumptionTariffInterval": "CIM100.IEC61968.PaymentMetering",
    "Vendor": "CIM100.IEC61968.PaymentMetering",
    "Cheque": "CIM100.IEC61968.PaymentMetering",
    "AccountMovement": "CIM100.IEC61968.PaymentMetering",
    "Shift": "CIM100.IEC61968.PaymentMetering",
    "Receipt": "CIM100.IEC61968.PaymentMetering",
    "Due": "CIM100.IEC61968.PaymentMetering",
    "BankAccountDetail": "CIM100.IEC61968.PaymentMetering",
    "AuxiliaryAccount": "CIM100.IEC61968.PaymentMetering",
    "Cashier": "CIM100.IEC61968.PaymentMetering",
    "Card": "CIM100.IEC61968.PaymentMetering",
    "MerchantAccount": "CIM100.IEC61968.PaymentMetering",
    "PointOfSale": "CIM100.IEC61968.PaymentMetering",
    "ProductAssetModel": "CIM100.IEC61968.Assets",
    "AssetModel": "CIM100.IEC61968.Assets",
    "Asset": "CIM100.IEC61968.Assets",
    "ComMedia": "CIM100.IEC61968.Assets",
    "AssetContainer": "CIM100.IEC61968.Assets",
    "AssetFunction": "CIM100.IEC61968.Assets",
    "Seal": "CIM100.IEC61968.Assets",
    "AssetInfo": "CIM100.IEC61968.Assets",
    "AcceptanceTest": "CIM100.IEC61968.Assets",
    "Work": "CIM100.IEC61968.Work",
    "Tariff": "CIM100.IEC61968.Customers",
    "CustomerAccount": "CIM100.IEC61968.Customers",
    "ServiceLocation": "CIM100.IEC61968.Customers",
    "CustomerAgreement": "CIM100.IEC61968.Customers",
    "ServiceCategory": "CIM100.IEC61968.Customers",
    "PricingStructure": "CIM100.IEC61968.Customers",
    "Customer": "CIM100.IEC61968.Customers",
    "ConnectDisconnectFunction": "CIM100.IEC61968.LoadControl",
    "RemoteConnectDisconnectInfo": "CIM100.IEC61968.LoadControl",
    "MarketParticipant": "CIM100.IEC62325",
    "IEC62325CIMVersion": "CIM100.IEC62325",
    "MarketRole": "CIM100.IEC62325",
    "PackageDependenciesCIMVeresion": "CIM100.PackageDependencies",
    "RotatingMachineDynamics": "CIM100.IEC61970.Dynamics",
    "SynchronousMachineTimeConstantReactance": "CIM100.IEC61970.Dynamics",
    "SynchronousMachineDynamics": "CIM100.IEC61970.Dynamics",
    "DynamicsFunctionBlock": "CIM100.IEC61970.Dynamics",
    "SynchronousMachineUserDefined": "CIM100.IEC61970.Dynamics",
    "SynchronousMachineDetailed": "CIM100.IEC61970.Dynamics",
    "SynchronousMachineSimplified": "CIM100.IEC61970.Dynamics",
    "SynchronousMachineEquivalentCircuit": "CIM100.IEC61970.Dynamics",
    "LinearShuntCompensator":"CIM100.IEC61970.Base.Wires"

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
