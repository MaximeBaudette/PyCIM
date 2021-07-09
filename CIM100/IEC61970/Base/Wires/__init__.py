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

"""An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

from CIM100.IEC61970.Base.Wires.PhaseImpedanceData import PhaseImpedanceData
from CIM100.IEC61970.Base.Wires.TapSchedule import TapSchedule
from CIM100.IEC61970.Base.Wires.TransformerStarImpedance import TransformerStarImpedance
from CIM100.IEC61970.Base.Wires.Recloser import Recloser
from CIM100.IEC61970.Base.Wires.RatioTapChangerTabularPoint import RatioTapChangerTabularPoint
from CIM100.IEC61970.Base.Wires.PhaseTapChangerTabular import PhaseTapChangerTabular
from CIM100.IEC61970.Base.Wires.RatioTapChanger import RatioTapChanger
from CIM100.IEC61970.Base.Wires.PhaseTapChangerLinear import PhaseTapChangerLinear
from CIM100.IEC61970.Base.Wires.ACLineSegment import ACLineSegment
from CIM100.IEC61970.Base.Wires.PowerTransformerEnd import PowerTransformerEnd
from CIM100.IEC61970.Base.Wires.Junction import Junction
from CIM100.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq
from CIM100.IEC61970.Base.Wires.Sectionaliser import Sectionaliser
from CIM100.IEC61970.Base.Wires.RatioTapChangerTabular import RatioTapChangerTabular
from CIM100.IEC61970.Base.Wires.PowerTransformer import PowerTransformer
from CIM100.IEC61970.Base.Wires.Fuse import Fuse
from CIM100.IEC61970.Base.Wires.EnergyConsumer import EnergyConsumer
from CIM100.IEC61970.Base.Wires.Disconnector import Disconnector
from CIM100.IEC61970.Base.Wires.Connector import Connector
from CIM100.IEC61970.Base.Wires.ReactiveCapabilityCurve import ReactiveCapabilityCurve
from CIM100.IEC61970.Base.Wires.Plant import Plant
from CIM100.IEC61970.Base.Wires.GroundDisconnector import GroundDisconnector
from CIM100.IEC61970.Base.Wires.Resistor import Resistor
from CIM100.IEC61970.Base.Wires.SynchronousMachine import SynchronousMachine
from CIM100.IEC61970.Base.Wires.PhaseTapChangerAsymetrical import PhaseTapChangerAsymetrical
from CIM100.IEC61970.Base.Wires.RectifierInverter import RectifierInverter
from CIM100.IEC61970.Base.Wires.SeriesCompensator import SeriesCompensator
from CIM100.IEC61970.Base.Wires.TapChangerControl import TapChangerControl
from CIM100.IEC61970.Base.Wires.RegulatingControl import RegulatingControl
from CIM100.IEC61970.Base.Wires.ProtectedSwitch import ProtectedSwitch
from CIM100.IEC61970.Base.Wires.PhaseTapChanger import PhaseTapChanger
from CIM100.IEC61970.Base.Wires.Ground import Ground
from CIM100.IEC61970.Base.Wires.CompositeSwitch import CompositeSwitch
from CIM100.IEC61970.Base.Wires.RegulationSchedule import RegulationSchedule
from CIM100.IEC61970.Base.Wires.TransformerTankEnd import TransformerTankEnd
from CIM100.IEC61970.Base.Wires.Breaker import Breaker
from CIM100.IEC61970.Base.Wires.MutualCoupling import MutualCoupling
from CIM100.IEC61970.Base.Wires.Line import Line
from CIM100.IEC61970.Base.Wires.PerLengthPhaseImpedance import PerLengthPhaseImpedance
from CIM100.IEC61970.Base.Wires.FrequencyConverter import FrequencyConverter
from CIM100.IEC61970.Base.Wires.ShuntCompensator import ShuntCompensator
from CIM100.IEC61970.Base.Wires.VoltageControlZone import VoltageControlZone
from CIM100.IEC61970.Base.Wires.LoadBreakSwitch import LoadBreakSwitch
from CIM100.IEC61970.Base.Wires.BusbarSection import BusbarSection
from CIM100.IEC61970.Base.Wires.TransformerEnd import TransformerEnd
from CIM100.IEC61970.Base.Wires.TransformerCoreAdmittance import TransformerCoreAdmittance
from CIM100.IEC61970.Base.Wires.StaticVarCompensator import StaticVarCompensator
from CIM100.IEC61970.Base.Wires.Switch import Switch
from CIM100.IEC61970.Base.Wires.PerLengthSequenceImpedance import PerLengthSequenceImpedance
from CIM100.IEC61970.Base.Wires.TransformerMeshImpedance import TransformerMeshImpedance
from CIM100.IEC61970.Base.Wires.SwitchSchedule import SwitchSchedule
from CIM100.IEC61970.Base.Wires.EnergySource import EnergySource
from CIM100.IEC61970.Base.Wires.TransformerTank import TransformerTank
from CIM100.IEC61970.Base.Wires.PhaseTapChangerTabularPoint import PhaseTapChangerTabularPoint
from CIM100.IEC61970.Base.Wires.DCLineSegment import DCLineSegment
from CIM100.IEC61970.Base.Wires.TapChanger import TapChanger
from CIM100.IEC61970.Base.Wires.Conductor import Conductor
from CIM100.IEC61970.Base.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear
from CIM100.IEC61970.Base.Wires.PhaseTapChangerSymetrical import PhaseTapChangerSymetrical
from CIM100.IEC61970.Base.Wires.Jumper import Jumper
from CIM100.IEC61970.Base.Wires.PowerElectronicsConnection import PowerElectronicsConnection
from CIM100.IEC61970.Base.Wires.PowerElectronicsConnectionPhase import PowerElectronicsConnectionPhase

nsURI = "http://iec.ch/TC57/2013/CIM-schema-CIM100#Wires"
nsPrefix = "cimWires"


class TapChangerKind(str):
    """Values are: voltageAndPhaseControl, phaseControl, fixed, voltageControl
    """
    pass

class WindingType(str):
    """Values are: tertiary, primary, secondary, quaternary
    """
    pass

class SynchronousMachineOperatingMode(str):
    """Values are: condenser, generator
    """
    pass

class TransformerControlMode(str):
    """Values are: reactive, volt
    """
    pass

class CoolantType(str):
    """Values are: air, hydrogenGas, water
    """
    pass

class SynchronousMachineType(str):
    """Values are: condenser, generator_or_condenser, generator
    """
    pass

class PhaseTapChangerKind(str):
    """Values are: unknown, asymmetrical, symmetrical
    """
    pass

class SVCControlMode(str):
    """Values are: off, voltage, reactivePower
    """
    pass

class RegulatingControlModeKind(str):
    """Values are: fixed, timeScheduled, voltage, admittance, reactivePower, powerFactor, currentFlow, activePower, temperature
    """
    pass

class WindingConnection(str):
    """Values are: Z, A, Yn, Y, Zn, D, I
    """
    pass

class CompositeSwitchType(str):
    """An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    """
    pass

class OperatingMode(str):
    """Textual name for an operating mode
    """
    pass
