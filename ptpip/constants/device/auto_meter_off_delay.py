from enum import Enum

# Indicates the time that is set in “Auto meter-off delay”
# of “AE lock timer – Power-offtime” in the custom menu
class AutoMeterOffDelay(Enum):
    Sec4    = 0x00
    Sec8    = 0x01
    Sec20   = 0x02
    Min1    = 0x03
    Min30   = 0x04
