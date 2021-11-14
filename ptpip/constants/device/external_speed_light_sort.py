from enum import Enum

class ExternalSpeedLightSort(Enum):
    CommunicationDisabled                               = 0x00
    Reserved                                            = 0x01
    NewTypeCommunicationWithSettingAndDisplaySection    = 0x02
    NewTypeCommunicationWithoutSettingAndDisplaySection = 0x03
