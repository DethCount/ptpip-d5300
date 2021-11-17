from enum import Enum

class InternalFlashManual(Enum):
    Full        = 0x00
    Half        = 0x01
    Quarter     = 0x02
    OneOver8    = 0x03
    OneOver16   = 0x04
    OneOver32   = 0x05
