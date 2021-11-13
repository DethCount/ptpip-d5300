from enum import Enum

# Indicates “AE lock timer – Remote control standby time”
# in the custom menu.
class RemoteControlDelay(Enum):
    Min1 = 0x00
    Min5 = 0x01
    Min10 = 0x02
    Min15 = 0x03
