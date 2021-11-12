from enum import Enum

class StillCaptureMode(Enum):
    SingleFrameShooting     = 0x0001
    ContinuousShooting      = 0x0002
    SelfTimer               = 0x8011 # @see BusrtNumber
    QuickResponseRemote     = 0x8014
    TwoSecondsDelayedRemote = 0x8015
    QuietShooting           = 0x8016
