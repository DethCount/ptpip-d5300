from enum import Enum

class ExposureDisplayStatus(Enum):
    NormalApertureAndNormalShutterSpeed = 0x00
    NormalApertureAndLowShutterSpeed = 0x01
    NormalApertureAndHighShutterSpeed = 0x02
    LowApertureAndNormalShutterSpeed = 0x03
    LowApertureAndLowShutterSpeed = 0x04
    LowApertureAndHighShutterSpeed = 0x05
    HighApertureAndNormalShutterSpeed = 0x06
    HighApertureAndLowShutterSpeed = 0x07
    HighApertureAndHighShutterSpeed = 0x08
