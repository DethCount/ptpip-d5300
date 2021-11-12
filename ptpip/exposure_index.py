from enum import Enum

class ExposureIndex(Enum):
    Lo1         = 0x0064
    Lo0Point7	= 0x007D
    Lo0Point3   = 0x00A0
    Iso200      = 0x00C8
    Iso250      = 0x00FA
    Iso320      = 0x0140
    Iso400      = 0x0190
    Iso500      = 0x01F4
    Iso640      = 0x0280
    Iso800      = 0x0320
    Iso1000     = 0x03E8
    Iso1250     = 0x04E2
    Iso1600     = 0x0640
    Iso2000     = 0x07D0
    Iso2500     = 0x09C4
    Iso3200     = 0x0C80
    Hi0Point3   = 0x0FA0
    Hi0Point7   = 0x1388
    Hi1         = 0x1900
