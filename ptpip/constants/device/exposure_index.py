from enum import Enum

class ExposureIndex(Enum):
    Undefined   = 0x0000
    Lo1         = 0x0064 # 100
    Lo0Point7	= 0x007D # 125
    Lo0Point3   = 0x00A0 # 160
    Iso200      = 0x00C8 # 200
    Iso250      = 0x00FA # 250
    Iso320      = 0x0140 # 320
    Iso400      = 0x0190 # 400
    Iso500      = 0x01F4 # 500
    Iso640      = 0x0280 # 640
    Iso800      = 0x0320 # 800
    Iso1000     = 0x03E8 # 1000
    Iso1250     = 0x04E2 # 1250
    Iso1600     = 0x0640 # 1600
    Iso2000     = 0x07D0 # 2000
    Iso2500     = 0x09C4 # 2500
    Iso3200     = 0x0C80 # 3200
    Hi0Point3   = 0x0FA0 # 4000
    Hi0Point7   = 0x1388 # 5000
    Hi1         = 0x1900 # 6400
    Iso8000     = 0x1F40 # 8000
    Iso10000    = 0x2710 # 10000
    Iso12800    = 0x3200 # 12800
    Iso16000    = 0x3E80 # 16000
    Iso20000    = 0x4E20 # 20000
    Iso25600    = 0x6400 # 25600
