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

"""The Generation Dynamics package contains prime movers, such as turbines and boilers, which are needed for simulation and educational purposes.
"""

from CIM100.IEC61970.Base.Generation.GenerationDynamics.BWRSteamSupply import BWRSteamSupply
from CIM100.IEC61970.Base.Generation.GenerationDynamics.HydroTurbine import HydroTurbine
from CIM100.IEC61970.Base.Generation.GenerationDynamics.SteamTurbine import SteamTurbine
from CIM100.IEC61970.Base.Generation.GenerationDynamics.SteamSupply import SteamSupply
from CIM100.IEC61970.Base.Generation.GenerationDynamics.FossilSteamSupply import FossilSteamSupply
from CIM100.IEC61970.Base.Generation.GenerationDynamics.Subcritical import Subcritical
from CIM100.IEC61970.Base.Generation.GenerationDynamics.PWRSteamSupply import PWRSteamSupply
from CIM100.IEC61970.Base.Generation.GenerationDynamics.PrimeMover import PrimeMover
from CIM100.IEC61970.Base.Generation.GenerationDynamics.CombustionTurbine import CombustionTurbine
from CIM100.IEC61970.Base.Generation.GenerationDynamics.HeatRecoveryBoiler import HeatRecoveryBoiler
from CIM100.IEC61970.Base.Generation.GenerationDynamics.Supercritical import Supercritical
from CIM100.IEC61970.Base.Generation.GenerationDynamics.DrumBoiler import DrumBoiler
from CIM100.IEC61970.Base.Generation.GenerationDynamics.CTTempActivePowerCurve import CTTempActivePowerCurve

nsURI = "http://iec.ch/TC57/2013/CIM-schema-CIM100#GenerationDynamics"
nsPrefix = "cimGenerationDynamics"


class TurbineType(str):
    """Values are: pelton, kaplan, francis
    """
    pass

class BoilerControlMode(str):
    """Values are: following, coordinated
    """
    pass
