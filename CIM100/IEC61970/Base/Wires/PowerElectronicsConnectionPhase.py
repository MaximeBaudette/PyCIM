from CIM100.IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
class PowerElectronicsConnectionPhase(PowerSystemResource):
    """"""

    def __init__(self, p=0.0, q=0.0, phase = None, *args, **kw_args):
        """Initialises a new 'PowerElectronicsConnection' instance.

        @param p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. 
        @param q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. 
        
        """
    
        #: 
        self.p = p

        #: 
        self.q = q

         elf._phase = None
        self.phase = phase
       
       
        super(PowerElectronicsConnectionPhase, self).__init__(*args, **kw_args)

    _attrs = ["p", "q"]
    _attr_types = {"p": float, "q": float}
    _defaults = {"p": 0.0, "q": 0.0}
    _enums = {"phase"}
    _refs = []
    _many_refs = []
