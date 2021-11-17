from enum import Enum

class WarningStatus(Enum):
    SequenceError           = 0x01
    BatteryInsufficient     = 0x02
    Reserved                = 0x04
    LensHardwareError       = 0x08
    iTTLError               = 0x10
    MinimumApertureWarning  = 0x20
    BulbWarning             = 0x40
    ChecksumError           = 0x80
