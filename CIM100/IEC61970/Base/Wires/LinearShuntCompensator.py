from CIM100.IEC61970.Base.Wires.ShuntCompensator import ShuntCompensator

class LinearShuntCompensator(ShuntCompensator):
    """
    """

    def __init__(self, b0PerSection=0.0, bPerSection=0.0, g0PerSection=0.0, gPerSection = 0.0, *args, **kw_args):
        """Initialises a new 'LinearShuntCompensator' instance.

        @param gPerSection: Positive sequence shunt (charging) conductance per section 
        @param b0PerSection: Zero sequence shunt (charging) susceptance per section 
        @param bPerSection: Positive sequence shunt (charging) susceptance per section 
        @param g0PerSection: Zero sequence shunt (charging) conductance per section 
        """
        
        #: Positive sequence shunt (charging) conductance per section
        self.gPerSection = gPerSection

        #: Zero sequence shunt (charging) susceptance per section
        self.b0PerSection = b0PerSection

        #: Positive sequence shunt (charging) susceptance per section
        self.bPerSection = bPerSection

        #: Zero sequence shunt (charging) conductance per section
        self.g0PerSection = g0PerSection

       

        super(LinearShuntCompensator, self).__init__(*args, **kw_args)