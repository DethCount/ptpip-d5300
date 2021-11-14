from enum import Enum

class AFModeSelect(Enum):
    AFS         = 0x00
    AFC         = 0x01
    AFA         = 0x02
    MFFixed     = 0x03
    MFSelection = 0x04
