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

from CIM100.IEC61970.Base.Generation.GenerationDynamics.FossilSteamSupply import FossilSteamSupply

class DrumBoiler(FossilSteamSupply):
    """Drum boilerDrum boiler
    """

    def __init__(self, drumBoilerRating=0.0, *args, **kw_args):
        """Initialises a new 'DrumBoiler' instance.

        @param drumBoilerRating: Rating of drum boiler in steam units 
        """
        #: Rating of drum boiler in steam units
        self.drumBoilerRating = drumBoilerRating

        super(DrumBoiler, self).__init__(*args, **kw_args)

    _attrs = ["drumBoilerRating"]
    _attr_types = {"drumBoilerRating": float}
    _defaults = {"drumBoilerRating": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

