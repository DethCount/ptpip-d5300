from enum import Enum

class VendorExtension(Enum):
    Undefined               = 0x00000000
    EastmanKodak            = 0x00000001
    SeikoEpson              = 0x00000002
    Agilent                 = 0x00000003
    Polaroid                = 0x00000004
    AgfaGevaert             = 0x00000005
    Microsoft               = 0x00000006
    Equinox                 = 0x00000007
    Viewquest               = 0x00000008
    STMicroelectronics      = 0x00000009
    Nikon                   = 0x0000000A
    Canon                   = 0x0000000B
    FotoNation              = 0x0000000C
    PENTAX                  = 0x0000000D
    Fuji                    = 0x0000000E
    Sony                    = 0x00000011
    NDD                     = 0x00000012 # NDD Medical Technologies
    Samsung                 = 0x0000001A
    Parrot                  = 0x0000001B
    Panasonic               = 0x0000001C
