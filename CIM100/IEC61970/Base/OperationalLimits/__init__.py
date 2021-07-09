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

"""The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""

from CIM100.IEC61970.Base.OperationalLimits.ApparentPowerLimit import ApparentPowerLimit
from CIM100.IEC61970.Base.OperationalLimits.ActivePowerLimit import ActivePowerLimit
from CIM100.IEC61970.Base.OperationalLimits.OperationalLimitType import OperationalLimitType
from CIM100.IEC61970.Base.OperationalLimits.BranchGroup import BranchGroup
from CIM100.IEC61970.Base.OperationalLimits.OperationalLimitSet import OperationalLimitSet
from CIM100.IEC61970.Base.OperationalLimits.ActivePowerLimitSet import ActivePowerLimitSet
from CIM100.IEC61970.Base.OperationalLimits.CurrentLimit import CurrentLimit
from CIM100.IEC61970.Base.OperationalLimits.CurrentLimitSet import CurrentLimitSet
from CIM100.IEC61970.Base.OperationalLimits.ApparentPowerLimitSet import ApparentPowerLimitSet
from CIM100.IEC61970.Base.OperationalLimits.BranchGroupTerminal import BranchGroupTerminal
from CIM100.IEC61970.Base.OperationalLimits.VoltageLimitSet import VoltageLimitSet
from CIM100.IEC61970.Base.OperationalLimits.VoltageLimit import VoltageLimit
from CIM100.IEC61970.Base.OperationalLimits.OperationalLimit import OperationalLimit

nsURI = "http://iec.ch/TC57/2013/CIM-schema-CIM100#OperationalLimits"
nsPrefix = "cimOperationalLimits"


class OperationalLimitDirectionKind(str):
    """Values are: low, high, absoluteValue
    """
    pass
