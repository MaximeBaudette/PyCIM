# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

pkg_map = {
    "Element": "cpsm",
    "Model": "cpsm",
    "IEC61970CIMVersion": "cpsm.iec61970",
    "GrossToNetActivePowerCurve": "cpsm.iec61970.generation.production",
    "HydroGeneratingUnit": "cpsm.iec61970.generation.production",
    "ThermalGeneratingUnit": "cpsm.iec61970.generation.production",
    "GeneratingUnit": "cpsm.iec61970.generation.production",
    "OperationalLimit": "cpsm.iec61970.operational_limits",
    "OperationalLimitSet": "cpsm.iec61970.operational_limits",
    "ActivePowerLimit": "cpsm.iec61970.operational_limits",
    "ApparentPowerLimit": "cpsm.iec61970.operational_limits",
    "VoltageLimit": "cpsm.iec61970.operational_limits",
    "CurrentLimit": "cpsm.iec61970.operational_limits",
    "PowerTransformer": "cpsm.iec61970.wires",
    "Disconnector": "cpsm.iec61970.wires",
    "SynchronousMachine": "cpsm.iec61970.wires",
    "BusbarSection": "cpsm.iec61970.wires",
    "ShuntCompensator": "cpsm.iec61970.wires",
    "LoadBreakSwitch": "cpsm.iec61970.wires",
    "RegulatingCondEq": "cpsm.iec61970.wires",
    "EnergyConsumer": "cpsm.iec61970.wires",
    "TransformerWinding": "cpsm.iec61970.wires",
    "RegulatingControl": "cpsm.iec61970.wires",
    "RegulationSchedule": "cpsm.iec61970.wires",
    "ACLineSegment": "cpsm.iec61970.wires",
    "Switch": "cpsm.iec61970.wires",
    "Conductor": "cpsm.iec61970.wires",
    "ReactiveCapabilityCurve": "cpsm.iec61970.wires",
    "TapChanger": "cpsm.iec61970.wires",
    "Line": "cpsm.iec61970.wires",
    "StaticVarCompensator": "cpsm.iec61970.wires",
    "SeriesCompensator": "cpsm.iec61970.wires",
    "Breaker": "cpsm.iec61970.wires",
    "DiscreteValue": "cpsm.iec61970.meas",
    "Measurement": "cpsm.iec61970.meas",
    "MeasurementValue": "cpsm.iec61970.meas",
    "MeasurementValueSource": "cpsm.iec61970.meas",
    "Analog": "cpsm.iec61970.meas",
    "AnalogValue": "cpsm.iec61970.meas",
    "MeasurementType": "cpsm.iec61970.meas",
    "Discrete": "cpsm.iec61970.meas",
    "LimitSet": "cpsm.iec61970.meas",
    "NonConformLoadGroup": "cpsm.iec61970.load_model",
    "ConformLoadSchedule": "cpsm.iec61970.load_model",
    "CustomerLoad": "cpsm.iec61970.load_model",
    "NonConformLoad": "cpsm.iec61970.load_model",
    "DayType": "cpsm.iec61970.load_model",
    "Season": "cpsm.iec61970.load_model",
    "Load": "cpsm.iec61970.load_model",
    "StationSupply": "cpsm.iec61970.load_model",
    "SeasonDayTypeSchedule": "cpsm.iec61970.load_model",
    "LoadGroup": "cpsm.iec61970.load_model",
    "EnergyArea": "cpsm.iec61970.load_model",
    "ConformLoadGroup": "cpsm.iec61970.load_model",
    "LoadArea": "cpsm.iec61970.load_model",
    "SubLoadArea": "cpsm.iec61970.load_model",
    "LoadResponseCharacteristic": "cpsm.iec61970.load_model",
    "NonConformLoadSchedule": "cpsm.iec61970.load_model",
    "InductionMotorLoad": "cpsm.iec61970.load_model",
    "ConformLoad": "cpsm.iec61970.load_model",
    "EquivalentNetwork": "cpsm.iec61970.equivalents",
    "EquivalentShunt": "cpsm.iec61970.equivalents",
    "EquivalentEquipment": "cpsm.iec61970.equivalents",
    "EquivalentBranch": "cpsm.iec61970.equivalents",
    "IdentifiedObject": "cpsm.iec61970.core",
    "Terminal": "cpsm.iec61970.core",
    "BaseVoltage": "cpsm.iec61970.core",
    "RegularIntervalSchedule": "cpsm.iec61970.core",
    "ConnectivityNodeContainer": "cpsm.iec61970.core",
    "Unit": "cpsm.iec61970.core",
    "EquipmentContainer": "cpsm.iec61970.core",
    "VoltageLevel": "cpsm.iec61970.core",
    "Bay": "cpsm.iec61970.core",
    "SubGeographicalRegion": "cpsm.iec61970.core",
    "RegularTimePoint": "cpsm.iec61970.core",
    "Equipment": "cpsm.iec61970.core",
    "Substation": "cpsm.iec61970.core",
    "Curve": "cpsm.iec61970.core",
    "PowerSystemResource": "cpsm.iec61970.core",
    "BasicIntervalSchedule": "cpsm.iec61970.core",
    "CurveData": "cpsm.iec61970.core",
    "GeographicalRegion": "cpsm.iec61970.core",
    "ConductingEquipment": "cpsm.iec61970.core",
    "ControlArea": "cpsm.iec61970.control_area",
    "TieFlow": "cpsm.iec61970.control_area",
    "ControlAreaGeneratingUnit": "cpsm.iec61970.control_area",
    "ConnectivityNode": "cpsm.iec61970.topology",
}