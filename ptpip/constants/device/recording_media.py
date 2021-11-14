from enum import Enum

# Indicates the recording destination of the images captured
# by using the shutter-release button of the camera.
class RecordingMedia(Enum):
    SDCard  = 0x00
    SDRAM   = 0x01
