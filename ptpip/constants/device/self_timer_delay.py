from enum import Enum

# Indicates “AE lock timer – Self-timer – The number of captured frames”
# in the custom menu.
class SelfTimerDelay(Enum):
    Sec2 = 0x00
    Sec5 = 0x01
    Sec10 = 0x02
    Sec20 = 0x03
