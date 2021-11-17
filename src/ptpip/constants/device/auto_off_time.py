from enum import Enum

# Indicates “AE lock timer – Power-off time” in the custom menu.
class AutoOffTime(Enum):
    Short       = 0x00
    Normal      = 0x01
    Long        = 0x02
    Customize   = 0x03
