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

from CIM100.IEC61970.Informative.InfGMLSupport.GmlDiagramObject import GmlDiagramObject

class GmlLineGeometry(GmlDiagramObject):
    """Typically used for rendering linear assets and/or power system resources.Typically used for rendering linear assets and/or power system resources.
    """

    def __init__(self, sourceSide='', *args, **kw_args):
        """Initialises a new 'GmlLineGeometry' instance.

        @param sourceSide: For dynamic network update (i.e. colouring) purposes 
        """
        #: For dynamic network update (i.e. colouring) purposes
        self.sourceSide = sourceSide

        super(GmlLineGeometry, self).__init__(*args, **kw_args)

    _attrs = ["sourceSide"]
    _attr_types = {"sourceSide": str}
    _defaults = {"sourceSide": ''}
    _enums = {}
    _refs = []
    _many_refs = []

