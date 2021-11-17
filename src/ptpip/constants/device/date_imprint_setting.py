from enum import Enum

# Indicates “Shooting, recording, and display – Date imprint setting”
# in the custom menu.
class DateImprintSetting(Enum):
    Off                 = 0x00
    YearMonthDate       = 0x01
    YearMonthDateTime   = 0x02
    BirthdayCounter     = 0x03
