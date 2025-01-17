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

from CIM100.IEC61970.Base.Core.BasicIntervalSchedule import BasicIntervalSchedule

class IrregularIntervalSchedule(BasicIntervalSchedule):
    """The schedule has TimePoints where the time between them varies.The schedule has TimePoints where the time between them varies.
    """

    def __init__(self, TimePoints=None, *args, **kw_args):
        """Initialises a new 'IrregularIntervalSchedule' instance.

        @param TimePoints: The point data values that define a curve
        """
        self._TimePoints = []
        self.TimePoints = [] if TimePoints is None else TimePoints

        super(IrregularIntervalSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TimePoints"]
    _many_refs = ["TimePoints"]

    def getTimePoints(self):
        """The point data values that define a curve
        """
        return self._TimePoints

    def setTimePoints(self, value):
        for x in self._TimePoints:
            x.IntervalSchedule = None
        for y in value:
            y._IntervalSchedule = self
        self._TimePoints = value

    TimePoints = property(getTimePoints, setTimePoints)

    def addTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj.IntervalSchedule = self

    def removeTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj.IntervalSchedule = None

