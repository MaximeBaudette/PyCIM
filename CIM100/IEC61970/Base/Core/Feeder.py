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

from CIM100.IEC61970.Base.Core.EquipmentContainer import EquipmentContainer
from CIM100.IEC61970.Base.Core.Substation import Substation

class Feeder(EquipmentContainer):
    """A new class for Feeder
    """

    def __init__(self, NormalEnergizingSubstation = None, Location = None, NormalHeadTerminal=None, *args, **kw_args):
        """Initialises a new 'Feeder' instance.

       
        """
        self._NormalEnergizingSubstation = None
        self.NormalEnergizingSubstation = NormalEnergizingSubstation

        self._Location = None
        self.Location = Location

        self._NormalHeadTerminal = []
        self.NormalHeadTerminal = [] if NormalHeadTerminal is None else NormalHeadTerminal

        super(Feeder, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["NormalEnergizedFeeder", "Location"]
    _many_refs = ["NormalEnergizedFeeder", "Location"]

    

