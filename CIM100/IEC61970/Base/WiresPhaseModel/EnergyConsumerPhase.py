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

from CIM100.IEC61970.Base.Core.PowerSystemResource import PowerSystemResource

class EnergyConsumerPhase(PowerSystemResource):

    def __init__(self, phase=None, EnergyConsumer=None, pfixed=0.0, p = 0.0, qfixed=0.0, q = 0.0, *args, **kw_args):
        """Initialises a new 'EnergyConsumerPhase' instance.

        @param phase:
        @param EnergyConsumer:
        """
        self.phase = phase
        self._EnergyConsumer = None
        self.EnergyConsumer = EnergyConsumer

        self.pfixed = pfixed
        self.p = p
        self.qfixed = qfixed
        self.q = q

        super(EnergyConsumerPhase, self).__init__(*args, **kw_args)

    _attrs = ["pfixed", "qfixed"]
    _attr_types = {"pfixed": float, "qfixed": float}
    _defaults = {"pfixed": 0.0, "qfixed": 0.0}
    _enums = {}
    _refs = ["EnergyConsumer"]
    _many_refs = []

    def getEnergyConsumer(self):
        
        return self._EnergyConsumer

    def setEnergyConsumer(self, value):
        if self._EnergyConsumer is not None:
            filtered = [x for x in self.EnergyConsumer.EnergyConsumerPhases if x != self]
            self._EnergyConsumer._EnergyConsumerPhases = filtered

        self._EnergyConsumer = value
        if self._EnergyConsumer is not None:
            if self not in self._EnergyConsumer._EnergyConsumerPhases:
                self._EnergyConsumer._EnergyConsumerPhases.append(self)

    EnergyConsumer = property(getEnergyConsumer, setEnergyConsumer)
