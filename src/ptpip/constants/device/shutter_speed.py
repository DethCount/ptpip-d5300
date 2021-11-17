from enum import Enum

# Upper 2 bytes: Numerator of the shutter speed
# Lower 2 bytes: Denominator of the shutter speed
# Except for Time and Bulb
class ShutterSpeed(Enum):
    Undefined       = 0x00000000
    OneOver4000     = 0x00010FA0 # 69536
    OneOver3200     = 0x00010C80 # 68736
    OneOver2500     = 0x000109C4 # 68036
    OneOver2000     = 0x000107D0 # 67536
    OneOver1600     = 0x00010640 # 67136
    OneOver1250     = 0x000104E2 # 66786
    OneOver1000     = 0x000103E8 # 66536
    OneOver800      = 0x00010320 # 66336
    OneOver640      = 0x00010280 # 66176
    OneOver500      = 0x000101F4 # 66036
    OneOver400      = 0x00010190 # 65936
    OneOver320      = 0x00010140 # 65856
    OneOver250      = 0x000100FA # 65786
    OneOver200      = 0x000100C8 # 65736
    OneOver160      = 0x000100A0 # 65696
    OneOver125      = 0x0001007D # 65661
    OneOver100      = 0x00010064 # 65636
    OneOver80       = 0x00010050 # 65616
    OneOver60       = 0x0001003C # 65596
    OneOver50       = 0x00010032 # 65586
    OneOver40       = 0x00010028 # 65576
    OneOver30       = 0x0001001E # 65566
    OneOver25       = 0x00010019 # 65561
    OneOver20       = 0x00010014 # 65556
    OneOver15       = 0x0001000F # 65551
    OneOver13       = 0x0001000D # 65549
    OneOver10       = 0x0001000A # 65546
    OneOver8        = 0x00010008 # 65544
    OneOver6        = 0x00010006 # 65542
    OneOver5        = 0x00010005 # 65541
    OneOver4        = 0x00010004 # 65540
    OneOver3        = 0x00010003 # 65539
    OneOver2Point5  = 0x000A0019 # 655385
    OneOver2        = 0x00010002 # 65538
    OneOver1Point6  = 0x000A0010 # 655376
    OneOver1Point3  = 0x000A000D # 655373
    One             = 0x00010001 # 65537
    OneBy1Point3    = 0x000D000A # 851978
    OneBy1Point6    = 0x0010000A # 1048586
    OneBy2          = 0x00020001 # 131073
    OneByZPoint5    = 0x0019000A # 1638410
    OneBy3          = 0x00030001 # 196609
    OneBy4          = 0x00040001 # 262145
    OneBy5          = 0x00050001 # 327681
    OneBy6          = 0x00060001 # 393217
    OneBy8          = 0x00080001 # 524289
    OneBy10         = 0x000A0001 # 655361
    OneBy13         = 0x000D0001 # 851969
    OneBy15         = 0x000F0001 # 983041
    OneBy20         = 0x00140001 # 1310721
    OneBy25         = 0x00190001 # 1638401
    OneBy30         = 0x001E0001 # 1966081
    Time            = 0xFFFFFFFD # 4294967293
    Bulb            = 0xFFFFFFFF # 4294967295

