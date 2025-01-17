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

"""The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

from CIM100.IEC61970.Base.Generation.Production.Reservoir import Reservoir
from CIM100.IEC61970.Base.Generation.Production.CogenerationPlant import CogenerationPlant
from CIM100.IEC61970.Base.Generation.Production.GenUnitOpSchedule import GenUnitOpSchedule
from CIM100.IEC61970.Base.Generation.Production.FuelAllocationSchedule import FuelAllocationSchedule
from CIM100.IEC61970.Base.Generation.Production.GrossToNetActivePowerCurve import GrossToNetActivePowerCurve
from CIM100.IEC61970.Base.Generation.Production.LevelVsVolumeCurve import LevelVsVolumeCurve
from CIM100.IEC61970.Base.Generation.Production.StartRampCurve import StartRampCurve
from CIM100.IEC61970.Base.Generation.Production.NuclearGeneratingUnit import NuclearGeneratingUnit
from CIM100.IEC61970.Base.Generation.Production.EmissionCurve import EmissionCurve
from CIM100.IEC61970.Base.Generation.Production.HydroPumpOpSchedule import HydroPumpOpSchedule
from CIM100.IEC61970.Base.Generation.Production.SteamSendoutSchedule import SteamSendoutSchedule
from CIM100.IEC61970.Base.Generation.Production.TargetLevelSchedule import TargetLevelSchedule
from CIM100.IEC61970.Base.Generation.Production.CombinedCyclePlant import CombinedCyclePlant
from CIM100.IEC61970.Base.Generation.Production.HeatRateCurve import HeatRateCurve
from CIM100.IEC61970.Base.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit
from CIM100.IEC61970.Base.Generation.Production.EmissionAccount import EmissionAccount
from CIM100.IEC61970.Base.Generation.Production.PenstockLossCurve import PenstockLossCurve
from CIM100.IEC61970.Base.Generation.Production.StartupModel import StartupModel
from CIM100.IEC61970.Base.Generation.Production.HydroGeneratingUnit import HydroGeneratingUnit
from CIM100.IEC61970.Base.Generation.Production.GenUnitOpCostCurve import GenUnitOpCostCurve
from CIM100.IEC61970.Base.Generation.Production.IncrementalHeatRateCurve import IncrementalHeatRateCurve
from CIM100.IEC61970.Base.Generation.Production.FossilFuel import FossilFuel
from CIM100.IEC61970.Base.Generation.Production.GeneratingUnit import GeneratingUnit
from CIM100.IEC61970.Base.Generation.Production.StartIgnFuelCurve import StartIgnFuelCurve
from CIM100.IEC61970.Base.Generation.Production.StartMainFuelCurve import StartMainFuelCurve
from CIM100.IEC61970.Base.Generation.Production.TailbayLossCurve import TailbayLossCurve
from CIM100.IEC61970.Base.Generation.Production.HydroPump import HydroPump
from CIM100.IEC61970.Base.Generation.Production.InflowForecast import InflowForecast
from CIM100.IEC61970.Base.Generation.Production.HydroGeneratingEfficiencyCurve import HydroGeneratingEfficiencyCurve
from CIM100.IEC61970.Base.Generation.Production.ShutdownCurve import ShutdownCurve
from CIM100.IEC61970.Base.Generation.Production.HydroPowerPlant import HydroPowerPlant
from CIM100.IEC61970.Base.Generation.Production.CAESPlant import CAESPlant
from CIM100.IEC61970.Base.Generation.Production.AirCompressor import AirCompressor
from CIM100.IEC61970.Base.Generation.Production.HeatInputCurve import HeatInputCurve
from CIM100.IEC61970.Base.Generation.Production.WindGeneratingUnit import WindGeneratingUnit

nsURI = "http://iec.ch/TC57/2013/CIM-schema-CIM100#Production"
nsPrefix = "cimProduction"


class FuelType(str):
    """Values are: oil, coal, lignite, gas
    """
    pass

class GeneratorOperatingMode(str):
    """Values are: MRN, EDC, LFC, fixed, REG, AGC, manual, off
    """
    pass

class GeneratorControlMode(str):
    """Values are: setpoint, pulse
    """
    pass

class HydroPlantType(str):
    """Values are: pumpedStorage, runOfRiver, minorStorage, majorStorage
    """
    pass

class HydroEnergyConversionKind(str):
    """Values are: generator, pumpAndGenerator
    """
    pass

class PenstockType(str):
    pass

class EmissionValueSource(str):
    """Values are: calculated, measured
    """
    pass

class GeneratorControlSource(str):
    """Values are: plantControl, offAGC, unavailable, onAGC
    """
    pass

class SpillwayGateType(str):
    pass

class SurgeTankCode(str):
    pass

class EmissionType(str):
    """Values are: carbonDisulfide, sulfurDioxide, hydrogenSulfide, chlorine, carbonDioxide, nitrogenOxide
    """
    pass

class Classification(str):
    """1..n, with 1 the most detailed, highest priority, etc.
    """
    pass

class HeatRate(float):
    """Heat generated, in energy pertime unit of elapsed time
    """
    pass

class CostPerHeatUnit(float):
    """Cost, in units of currency, per quantity of heat generated
    """
    pass

class Emission(float):
    """Quantity of emission per fuel heat content
    """
    pass
