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

from CIM100.IEC61970.Graphics.DiagramObject import DiagramObject

class TextDiagramObject(DiagramObject):
    """A diagram object for placing free-text or text derived from an associated domain object.A diagram object for placing free-text or text derived from an associated domain object.
    """

    def __init__(self, text='', *args, **kw_args):
        """Initialises a new 'TextDiagramObject' instance.

        @param text: The text that is displayed by this text diagram object 
        """
        #: The text that is displayed by this text diagram object
        self.text = text

        super(TextDiagramObject, self).__init__(*args, **kw_args)

    _attrs = ["text"]
    _attr_types = {"text": str}
    _defaults = {"text": ''}
    _enums = {}
    _refs = []
    _many_refs = []

