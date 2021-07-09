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

from CIM100.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq

class PowerElectronicsConnection(RegulatingCondEq):
    """A connection to the AC network for energy production or consumption that uses power electronics rather than rotating machines."""

    def __init__(self, inverterMode = None, maxIFault = 0.0, maxQ=0.0, minQ=0.0, p=0.0, q=0.0, r=0.0, r0=0.0, ratedS=0.0, ratedU=0.0, rn=0.0, x=0.0, x0=0.0, xn=0.0, PowerElectronicsConnectionPhases=None, PowerElectronicsUnit=None, *args, **kw_args):
        """Initialises a new 'PowerElectronicsConnection' instance.

        @param maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param minQ: Minimum reactive power limit for the unit. This is the minimum (nameplate) limit for the unit.
        @param p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. 
        @param q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. 
        @param r: Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909. 
        @param r0: Zero sequence resistance of the synchronous machine. 
        @param ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value. 
        @param ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909. 
        @param rn: Negative sequence Thevenin resistance.
        @param x0: Zero sequence Thevenin reactance. 
        @param xn: Negative sequence Thevenin reactance.
        """
        #:
        self.inverterMode = inverterMode

        self.maxIFault = maxIFault

        #: 
        self.maxQ = maxQ

        #: 
        self.minQ = minQ

        #: 
        self.p = p

        #: 
        self.q = q

        #: 
        self.ratedS = ratedS

        #: 
        self.ratedU = ratedU

         #: 
        self.r = r

        #: 
        self.r0 = r0

        #: 
        self.rn = rn

        #: 
        self.x = x

        #: 
        self.x0 = x0

        #: 
        self.xn = xn

        self._PowerElectronicsConnectionPhases = []
        self.PowerElectronicsConnectionPhases = [] if PowerElectronicsConnectionPhases is None else PowerElectronicsConnectionPhases

        self._PowerElectronicsUnit = []
        self.PowerElectronicsUnit = [] if PowerElectronicsUnit is None else PowerElectronicsUnit
       
        super(PowerElectronicsConnection, self).__init__(*args, **kw_args)

    _attrs = ["maxIFault", "maxQ", "minQ", "p", "q", "r", "r0", "ratedS", "ratedU", "rn", "x", "x0", "xn"]
    _attr_types = {"maxIFault": float, "maxQ": float, "minQ": float, "p": float, "q": float, "r": float, "r0": float, "ratedS": float, "ratedU": float, "rn": float,"x": float, "x0": float, "xn": float}
    _defaults = {"maxQ": 0.0, "minQ": 0.0, "p": 0.0, "q": 0.0, "r": 0.0, "r0": 0.0, "ratedS": 0.0, "ratedU": 0.0, "rn": 0.0,"x": 0.0, "x0": 0.0, "xn": 0.0}
    _enums = {"inverterMode"}
    _refs = []
    _many_refs = ["PowerElectronicsConnectionPhases","PowerElectronicsUnit"]


