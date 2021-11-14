from enum import Enum

class BracketingType(Enum):
    Undefined       = 0x00
    AEBracketing    = 0x01
    Reserved        = 0x02
    WBBracketing    = 0x03
    ADLBracketing   = 0x04
