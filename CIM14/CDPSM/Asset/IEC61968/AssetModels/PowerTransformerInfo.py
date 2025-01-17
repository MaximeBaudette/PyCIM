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

from CIM14.CDPSM.Asset.IEC61968.Assets.AssetInfo import AssetInfo

class PowerTransformerInfo(AssetInfo):
    """Set of power transformer data, from an equipment library.
    """

    def __init__(self, TransformerTankInfo=None, *args, **kw_args):
        """Initialises a new 'PowerTransformerInfo' instance.

        @param TransformerTankInfo: Data for all the tanks described by this power transformer data.
        """
        self._TransformerTankInfo = []
        self.TransformerTankInfo = [] if TransformerTankInfo is None else TransformerTankInfo

        super(PowerTransformerInfo, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TransformerTankInfo"]
    _many_refs = ["TransformerTankInfo"]

    def getTransformerTankInfo(self):
        """Data for all the tanks described by this power transformer data.
        """
        return self._TransformerTankInfo

    def setTransformerTankInfo(self, value):
        for x in self._TransformerTankInfo:
            x.PowerTransformerInfo = None
        for y in value:
            y._PowerTransformerInfo = self
        self._TransformerTankInfo = value

    TransformerTankInfo = property(getTransformerTankInfo, setTransformerTankInfo)

    def addTransformerTankInfo(self, *TransformerTankInfo):
        for obj in TransformerTankInfo:
            obj.PowerTransformerInfo = self

    def removeTransformerTankInfo(self, *TransformerTankInfo):
        for obj in TransformerTankInfo:
            obj.PowerTransformerInfo = None

