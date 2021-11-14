from enum import Enum

# Indicates the picture control item whose setting is currently valid.
class ActivePicCtrlItem(Enum):
    Standard    = 0x01
    Neutral     = 0x02
    Vivid       = 0x03
    Monochrome  = 0x04
    Portrait    = 0x05
    Landscape   = 0x06

    Option1     = 0x65
    Option2     = 0x66
    Option3     = 0x67
    Option4     = 0x68

    Custom1     = 0xC9
    Custom2     = 0xCA
    Custom3     = 0xCB
    Custom4     = 0xCC
    Custom5     = 0xCD
    Custom6     = 0xCE
    Custom7     = 0xCF
    Custom8     = 0xD0
    Custom9     = 0xD1
