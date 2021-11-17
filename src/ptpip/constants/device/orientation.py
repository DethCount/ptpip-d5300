from enum import Enum

class Orientation(Enum):
    NormalOrUndefined   = 0x00
    GripSideUpward      = 0x01
    GripSideDownward    = 0x02
    UpsideDown          = 0x03
