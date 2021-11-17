from enum import Enum

class AEBracketingStep(Enum):
    OneThirdEV      = 0x00
    OneHalfEV       = 0x01
    TwoHalvesEV     = 0x02
    OneEV           = 0x03
    FourThirdsEV    = 0x04
    ThreeHalvesEV   = 0x05
    FiveThirdsEV    = 0x06
    TwoEV           = 0x07
