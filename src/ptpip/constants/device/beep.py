from enum import Enum

# Indicates “Shooting, recording, and display - Beep setting”
# in the custom menu
class Beep(Enum):
    HighTone    = 0x00
    LowTone     = 0x01
    NoBeeping   = 0x02
