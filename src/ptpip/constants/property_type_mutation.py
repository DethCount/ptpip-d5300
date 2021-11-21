from enum import Enum

class PropertyTypeMutation(Enum):
    Undefined   = 0x0
    Range       = 0x1
    Enumeration = 0x2
    Time        = 0x3
    Array       = 0x4
    RegExp      = 0x5
    ByteString  = 0x6
    Text        = 0x7
