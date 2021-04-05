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

from CIM100.IEC61970.Core.IdentifiedObject import IdentifiedObject

class LoadGroup(IdentifiedObject):
    """The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    def __init__(self, SubLoadArea=None, *args, **kw_args):
        """Initialises a new 'LoadGroup' instance.

        @param SubLoadArea: The SubLoadArea where the Loadgroup belongs.
        """
        self._SubLoadArea = None
        self.SubLoadArea = SubLoadArea

        super(LoadGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SubLoadArea"]
    _many_refs = []

    def getSubLoadArea(self):
        """The SubLoadArea where the Loadgroup belongs.
        """
        return self._SubLoadArea

    def setSubLoadArea(self, value):
        if self._SubLoadArea is not None:
            filtered = [x for x in self.SubLoadArea.LoadGroups if x != self]
            self._SubLoadArea._LoadGroups = filtered

        self._SubLoadArea = value
        if self._SubLoadArea is not None:
            if self not in self._SubLoadArea._LoadGroups:
                self._SubLoadArea._LoadGroups.append(self)

    SubLoadArea = property(getSubLoadArea, setSubLoadArea)

