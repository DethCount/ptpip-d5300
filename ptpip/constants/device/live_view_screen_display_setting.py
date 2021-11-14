from enum import Enum

# Indicates the choice of “Shooting, recording, and display
# – Live view screen display setting”
# in the custom menu.
class LiveViewScreenDisplaySetting(Enum):
    AllInvalid                  = 0x00
    InformationDisplayOn        = 0x01
    InformationDisplayOff       = 0x02
    GridDisplay                 = 0x04
    InformationScreenDisplay    = 0x08
    AllValid                    = 0x0F
