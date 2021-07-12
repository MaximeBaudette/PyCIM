from CIM100.IEC61970.Base.Core.Equipment import Equipment

class PowerElectronicsUnit(Equipment):
    """
    """

    def __init__(self, maxP=0.0, minP=0.0, *args, **kw_args):
        """Initialises a new 'PowerElectronicsUnit' instance.

        @param maxP
        @param minP
        """
        self.maxP = maxP

        self.minPO = minP

        super(PowerElectronicsUnit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BaseVoltage", "ClearanceTags", "ProtectionEquipments", "Terminals", "OutageStepRoles", "SvStatus"]
    _many_refs = ["ClearanceTags", "ProtectionEquipments", "Terminals", "OutageStepRoles"]
