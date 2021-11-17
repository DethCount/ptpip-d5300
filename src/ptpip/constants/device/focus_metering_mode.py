from enum import Enum

class FocusMeteringMode(Enum):
    Undefined           = 0x0000
    DynamicAFMode       = 0x0002

    SinglePointAFMode   = 0x8010
    AutoAreaAFMode      = 0x8011
    Tracking3D11Points  = 0x8012
