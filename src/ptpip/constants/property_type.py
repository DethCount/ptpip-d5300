from enum import Enum

class PropertyType(Enum):
    Undefined       = 0x0000
    Int8            = 0x0001
    Uint8           = 0x0002
    Int16           = 0x0003
    Uint16          = 0x0004
    Int32           = 0x0005
    Uint32          = 0x0006
    Int64           = 0x0007
    Uint64          = 0x0008
    Int128          = 0x0009
    Uint128         = 0x000A

    Int8Array       = 0x4001
    Uint8Array      = 0x4002
    Int16Array      = 0x4003
    Uint16Array     = 0x4004
    Int32Array      = 0x4005
    Uint32Array     = 0x4006
    Int64Array      = 0x4007
    Uint64Array     = 0x4008
    Int128Array     = 0x4009
    Uint128Array    = 0x400A

    String          = 0xFFFF
