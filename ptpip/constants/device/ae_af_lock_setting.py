from enum import Enum

# Indicates “Operation – Function of the AE-L/AF-L button”
# in the custom menu.
class AEAFLockSetting(Enum):
    AELAndAFL   = 0x00
    AEL         = 0x01
    AFL         = 0x02
    AELHold     = 0x03
    AFOn        = 0x04
