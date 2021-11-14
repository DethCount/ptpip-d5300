from enum import Enum

# Indicates the choice of “Shooting, recording, and display
# - Date imprint setting –Birthday counter”
# in the custom menu.
class DateCounterSelect(Enum):
    First   = 0x00
    Second  = 0x01
    Third   = 0x02
