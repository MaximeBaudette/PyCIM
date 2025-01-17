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

from CIM100.Element import Element

class NameType(Element):
    """Type of name. Possible values for attribute 'name' are implementation dependent but standard profiles may specify types. An enterprise may have multiple IT systems each having its own local name for the same object, e.g. a planning system may have different names from an EMS. An object may also have different names within the same IT system, e.g. localName and aliasName as defined in CIM version 14. Their definitions from CIM14 are The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. localName: A free text name local to a node in a naming hierarchy similar to a file directory structure. A power system related naming hierarchy may be: Substation, VoltageLevel, Equipment etc. Children of the same parent in such a hierarchy have names that typically are unique among them. aliasName: A free text alternate name typically used in tabular reports where the column width is limited.Type of name. Possible values for attribute 'name' are implementation dependent but standard profiles may specify types. An enterprise may have multiple IT systems each having its own local name for the same object, e.g. a planning system may have different names from an EMS. An object may also have different names within the same IT system, e.g. localName and aliasName as defined in CIM version 14. Their definitions from CIM14 are The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. localName: A free text name local to a node in a naming hierarchy similar to a file directory structure. A power system related naming hierarchy may be: Substation, VoltageLevel, Equipment etc. Children of the same parent in such a hierarchy have names that typically are unique among them. aliasName: A free text alternate name typically used in tabular reports where the column width is limited.
    """

    def __init__(self, name='', description='', Names=None, NameTypeAuthority=None, *args, **kw_args):
        """Initialises a new 'NameType' instance.

        @param name: Name of the name type. 
        @param description: Description of the name type. 
        @param Names: All names of this type.
        @param NameTypeAuthority: Authority responsible for managing names of this type.
        """
        #: Name of the name type.
        self.name = name

        #: Description of the name type.
        self.description = description

        self._Names = []
        self.Names = [] if Names is None else Names

        self._NameTypeAuthority = None
        self.NameTypeAuthority = NameTypeAuthority

        super(NameType, self).__init__(*args, **kw_args)

    _attrs = ["name", "description"]
    _attr_types = {"name": str, "description": str}
    _defaults = {"name": '', "description": ''}
    _enums = {}
    _refs = ["Names", "NameTypeAuthority"]
    _many_refs = ["Names"]

    def getNames(self):
        """All names of this type.
        """
        return self._Names

    def setNames(self, value):
        for x in self._Names:
            x.NameType = None
        for y in value:
            y._NameType = self
        self._Names = value

    Names = property(getNames, setNames)

    def addNames(self, *Names):
        for obj in Names:
            obj.NameType = self

    def removeNames(self, *Names):
        for obj in Names:
            obj.NameType = None

    def getNameTypeAuthority(self):
        """Authority responsible for managing names of this type.
        """
        return self._NameTypeAuthority

    def setNameTypeAuthority(self, value):
        if self._NameTypeAuthority is not None:
            filtered = [x for x in self.NameTypeAuthority.NameTypes if x != self]
            self._NameTypeAuthority._NameTypes = filtered

        self._NameTypeAuthority = value
        if self._NameTypeAuthority is not None:
            if self not in self._NameTypeAuthority._NameTypes:
                self._NameTypeAuthority._NameTypes.append(self)

    NameTypeAuthority = property(getNameTypeAuthority, setNameTypeAuthority)

