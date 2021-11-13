from enum import Enum

class LCDPowerOff(Enum):
    Sec8    = 0x00
    Sec12   = 0x01
    Sec20   = 0x02
    Min1    = 0x03
    Min10   = 0x04
