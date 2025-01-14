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

from CIM100.IEC61970.Base.Wires.PhaseTapChanger import PhaseTapChanger

class PhaseTapChangerNonLinear(PhaseTapChanger):
    """PhaseTapChangerNonLinear describe the non linear behavior of a phase tap changer. This is a base class for the symmetrical and asymmetrical models. The details of these models can be found in the IEC 61970-301 document.PhaseTapChangerNonLinear describe the non linear behavior of a phase tap changer. This is a base class for the symmetrical and asymmetrical models. The details of these models can be found in the IEC 61970-301 document.
    """

    def __init__(self, xMedian=0.0, voltageStepIncrement=0.0, xMax=0.0, *args, **kw_args):
        """Initialises a new 'PhaseTapChangerNonLinear' instance.

        @param xMedian: The reactance at the mid tap step. 
        @param voltageStepIncrement: The voltage step increment on the out of phase winding. This voltage step on the out of phase winding of the phase shifter. 
        @param xMax: The reactance at the maximum tap step. 
        """
        #: The reactance at the mid tap step.
        self.xMedian = xMedian

        #: The voltage step increment on the out of phase winding. This voltage step on the out of phase winding of the phase shifter.
        self.voltageStepIncrement = voltageStepIncrement

        #: The reactance at the maximum tap step.
        self.xMax = xMax

        super(PhaseTapChangerNonLinear, self).__init__(*args, **kw_args)

    _attrs = ["xMedian", "voltageStepIncrement", "xMax"]
    _attr_types = {"xMedian": float, "voltageStepIncrement": float, "xMax": float}
    _defaults = {"xMedian": 0.0, "voltageStepIncrement": 0.0, "xMax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

