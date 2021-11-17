from enum import Enum

class FocusMode(Enum):
    Undefined              = 0x0000
    ManualFocus            = 0x0001

    SingleAFServo          = 0x8010
    ContinuousAFServo      = 0x8011
    AFServoModeAutoSwitch  = 0x8012
