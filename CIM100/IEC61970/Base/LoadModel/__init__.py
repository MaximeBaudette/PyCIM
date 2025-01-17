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

"""This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

from CIM100.IEC61970.Base.LoadModel.ConformLoad import ConformLoad
from CIM100.IEC61970.Base.LoadModel.ConformLoadGroup import ConformLoadGroup
from CIM100.IEC61970.Base.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
from CIM100.IEC61970.Base.LoadModel.LoadGroup import LoadGroup
from CIM100.IEC61970.Base.LoadModel.ConformLoadSchedule import ConformLoadSchedule
from CIM100.IEC61970.Base.LoadModel.LoadArea import LoadArea
from CIM100.IEC61970.Base.LoadModel.PowerCutZone import PowerCutZone
from CIM100.IEC61970.Base.LoadModel.LoadResponseCharacteristic import LoadResponseCharacteristic
from CIM100.IEC61970.Base.LoadModel.NonConformLoad import NonConformLoad
from CIM100.IEC61970.Base.LoadModel.StationSupply import StationSupply
from CIM100.IEC61970.Base.LoadModel.EnergyArea import EnergyArea
from CIM100.IEC61970.Base.LoadModel.NonConformLoadSchedule import NonConformLoadSchedule
from CIM100.IEC61970.Base.LoadModel.NonConformLoadGroup import NonConformLoadGroup
from CIM100.IEC61970.Base.LoadModel.DayType import DayType
from CIM100.IEC61970.Base.LoadModel.SubLoadArea import SubLoadArea
from CIM100.IEC61970.Base.LoadModel.Season import Season

nsURI = "http://iec.ch/TC57/2013/CIM-schema-CIM100#LoadModel"
nsPrefix = "cimLoadModel"


class SeasonName(str):
    """Values are: winter, summer, fall, spring
    """
    pass
