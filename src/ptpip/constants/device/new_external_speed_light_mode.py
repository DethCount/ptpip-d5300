from enum import Enum

class NewExternalSpeedLightMode(Enum):
    Off                                 = 0x00
    iTTLBL                              = 0x01
    iTTL                                = 0x02
    ApertureInterlockingAutomaticFlash  = 0x03
    ExternalAutomaticFlash              = 0x04
    ManualDistancePriority              = 0x05
    Manual                              = 0x06
    MultiFlash                          = 0x07
