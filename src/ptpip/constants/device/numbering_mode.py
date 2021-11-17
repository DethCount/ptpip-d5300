from enum import Enum

# Indicates “Shooting, recording, and display – Sequential numbering mode”
# in the custom menu.
class NumberingMode(Enum):
    Off     = 0x00
    On      = 0x01
    Reset   = 0x02
