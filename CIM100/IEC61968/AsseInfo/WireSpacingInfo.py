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

from CIM100.IEC61968.Assets.AssetInfo import AssetInfo

class WireSpacingInfo(AssetInfo):
    """Wire spacing data that associates multiple wire positions with the line segment, and allows to calculate line segment impedances. Number of phases can be derived from the number of associated wire positions whose phase is not neutral. 
    """


    def __init__(self, isCable=False, phaseWireCount=1, phaseWireSpacing = 1, usage="secondary", *args, **kw_args):
        """Initialises a new 'ConductorInfo' instance.

        @param isCable: If true, this spacing data describes a cable.
        @param phaseWireCount: Number of wire sub-conductors in the symmetrical bundle (typically between 1 and 4).
        @param phaseWireSpacine: Distance between wire sub-conductors in a symmetrical bundle.
        @param usage: Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        """
        #: If true, this spacing data describes a cable
        self.isCable = isCable

        #: Number of wire sub-conductors in the symmetrical bundle (typically between 1 and 4).
        self.phaseWireCount =  phaseWireCount

        #: Distance between wire sub-conductors in a symmetrical bundle.
        self.phaseWireSpacine = phaseWireSpacing

        #: Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        self.usage = usage

        super(WireSpacingInfo, self).__init__(*args, **kw_args)

    _attrs = ["isCable", "phaseWireCount", "phaseWireSpacine", "usage"]
    _attr_types = {"isCable": bool, "phaseWireCount": int, "phaseWireSpacine": float,  "usage": str}
    _defaults = {"isCable": False, "phaseWireCount": 1, "phaseWireSpacine": 0.0,  "usage": "distribution"}
    _enums = {"usage": "WireUsageKind"}