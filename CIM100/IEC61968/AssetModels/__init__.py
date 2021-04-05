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

"""This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized AssetInfo subclasses. They hold attributes that can be referenced by not only Asset-s or AssetModel-s but also by ConductingEquipment-s.
"""

from CIM100.IEC61968.AssetModels.ShortCircuitTest import ShortCircuitTest
from CIM100.IEC61968.AssetModels.EndDeviceInfo import EndDeviceInfo
from CIM100.IEC61968.AssetModels.WireType import WireType
from CIM100.IEC61968.AssetModels.TapeShieldCableInfo import TapeShieldCableInfo
from CIM100.IEC61968.AssetModels.ConductorInfo import ConductorInfo
from CIM100.IEC61968.AssetModels.TapChangerInfo import TapChangerInfo
from CIM100.IEC61968.AssetModels.TransformerTankInfo import TransformerTankInfo
from CIM100.IEC61968.AssetModels.PowerTransformerInfo import PowerTransformerInfo
from CIM100.IEC61968.AssetModels.OpenCircuitTest import OpenCircuitTest
from CIM100.IEC61968.AssetModels.CableInfo import CableInfo
from CIM100.IEC61968.AssetModels.TransformerEndInfo import TransformerEndInfo
from CIM100.IEC61968.AssetModels.NoLoadTest import NoLoadTest
from CIM100.IEC61968.AssetModels.OverheadConductorInfo import OverheadConductorInfo
from CIM100.IEC61968.AssetModels.ConcentricNeutralCableInfo import ConcentricNeutralCableInfo
from CIM100.IEC61968.AssetModels.WireArrangement import WireArrangement
from CIM100.IEC61968.AssetModels.TransformerTest import TransformerTest

nsURI = "http://iec.ch/TC57/2013/CIM-schema-CIM100#AssetModels"
nsPrefix = "cimAssetModels"


class CableOuterJacketKind(str):
    """Values are: pvc, linearLowDensityPolyethylene, none, insulating, other, polyethylene, semiconducting
    """
    pass

class ConductorMaterialKind(str):
    """Values are: aluminum, copper, other, steel, acsr
    """
    pass

class ConductorUsageKind(str):
    """Values are: secondary, other, distribution, transmission
    """
    pass

class CableConstructionKind(str):
    """Values are: sector, other, solid, compacted, stranded, segmental, compressed
    """
    pass

class CableShieldMaterialKind(str):
    """Values are: lead, aluminum, other, copper, steel
    """
    pass

class ConductorInsulationKind(str):
    """Values are: treeRetardantCrosslinkedPolyethylene, butyl, highPressureFluidFilled, other, varnishedCambricCloth, siliconRubber, beltedPilc, crosslinkedPolyethylene, oilPaper, lowCapacitanceRubber, asbestosAndVarnishedCambric, treeResistantHighMolecularWeightPolyethylene, unbeltedPilc, ozoneResistantRubber, ethylenePropyleneRubber, highMolecularWeightPolyethylene, varnishedDacronGlass, rubber
    """
    pass
