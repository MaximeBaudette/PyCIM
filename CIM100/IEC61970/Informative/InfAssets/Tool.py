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

from CIM100.IEC61968.Assets.Asset import Asset

class Tool(Asset):
    """Tool asset.Tool asset.
    """

    def __init__(self, lastCalibrationDate='', Crew=None, *args, **kw_args):
        """Initialises a new 'Tool' instance.

        @param lastCalibrationDate: Date the tool was last caibrated, if applicable. 
        @param Crew:
        """
        #: Date the tool was last caibrated, if applicable.
        self.lastCalibrationDate = lastCalibrationDate

        self._Crew = None
        self.Crew = Crew

        super(Tool, self).__init__(*args, **kw_args)

    _attrs = ["lastCalibrationDate"]
    _attr_types = {"lastCalibrationDate": str}
    _defaults = {"lastCalibrationDate": ''}
    _enums = {}
    _refs = ["Crew"]
    _many_refs = []

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.Tools if x != self]
            self._Crew._Tools = filtered

        self._Crew = value
        if self._Crew is not None:
            if self not in self._Crew._Tools:
                self._Crew._Tools.append(self)

    Crew = property(getCrew, setCrew)

