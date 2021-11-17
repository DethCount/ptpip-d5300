from enum import Enum

# Indicates “Operation – +/- direction of the indicator display”
# in the custom menu.
class IndicatorDisplay(Enum):
    PlusMinus   = 0x00
    MinusPlus   = 0x01
