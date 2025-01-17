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

from CIM100.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class ConnectivityNode(IdentifiedObject):
    """Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    def __init__(self, TopologicalNode=None, ConnectivityNodeContainer=None, Terminals=None, OperationalLimitSet=None, *args, **kw_args):
        """Initialises a new 'ConnectivityNode' instance.

        @param TopologicalNode: Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        @param ConnectivityNodeContainer: Container of this connectivity node.
        @param Terminals: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        self._ConnectivityNodeContainer = None
        self.ConnectivityNodeContainer = ConnectivityNodeContainer

        self._Terminals = []
        self.Terminals = [] if Terminals is None else Terminals

        self._OperationalLimitSet = None
        self.OperationalLimitSet = OperationalLimitSet

        super(ConnectivityNode, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TopologicalNode", "ConnectivityNodeContainer", "Terminals", "OperationalLimitSet"]
    _many_refs = ["Terminals"]

    def getTopologicalNode(self):
        """Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            filtered = [x for x in self.TopologicalNode.ConnectivityNodes if x != self]
            self._TopologicalNode._ConnectivityNodes = filtered

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            if self not in self._TopologicalNode._ConnectivityNodes:
                self._TopologicalNode._ConnectivityNodes.append(self)

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def getConnectivityNodeContainer(self):
        """Container of this connectivity node.
        """
        return self._ConnectivityNodeContainer

    def setConnectivityNodeContainer(self, value):
        if self._ConnectivityNodeContainer is not None:
            filtered = [x for x in self.ConnectivityNodeContainer.ConnectivityNodes if x != self]
            self._ConnectivityNodeContainer._ConnectivityNodes = filtered

        self._ConnectivityNodeContainer = value
        if self._ConnectivityNodeContainer is not None:
            if self not in self._ConnectivityNodeContainer._ConnectivityNodes:
                self._ConnectivityNodeContainer._ConnectivityNodes.append(self)

    ConnectivityNodeContainer = property(getConnectivityNodeContainer, setConnectivityNodeContainer)

    def getTerminals(self):
        """Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._Terminals

    def setTerminals(self, value):
        for x in self._Terminals:
            x.ConnectivityNode = None
        for y in value:
            y._ConnectivityNode = self
        self._Terminals = value

    Terminals = property(getTerminals, setTerminals)

    def addTerminals(self, *Terminals):
        for obj in Terminals:
            obj.ConnectivityNode = self

    def removeTerminals(self, *Terminals):
        for obj in Terminals:
            obj.ConnectivityNode = None

