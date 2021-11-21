from enum import Enum

class StillCaptureMode(Enum):
    Undefined               = 0x0000
    SingleFrameShooting     = 0x0001
    Burst                   = 0x0002 # ContinuousShootingH
    Timelapse               = 0x0003

    ContinuousShootingL     = 0x8010
    SelfTimer               = 0x8011 # @see BusrtNumber
    QuickResponseRemote     = 0x8014
    TwoSecondsDelayedRemote = 0x8015
    QuietShooting           = 0x8016
