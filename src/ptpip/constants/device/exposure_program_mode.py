from enum import Enum

class ExposureProgramMode(Enum):
    Undefined                       = 0x0000
    Manual                          = 0x0001
    ProgramAuto                     = 0x0002
    AperturePriorityAuto            = 0x0003
    ShutterPriorityAuto             = 0x0004
    SceneModeAuto                   = 0x8010
    SceneModePortrait               = 0x8011
    SceneModeLandscape              = 0x8012
    SceneModeCloseUp                = 0x8013
    SceneModeSports                 = 0x8014
    SceneModeNightPortrait          = 0x8015
    SceneModeFlashProhibitionAuto   = 0x8016
    SceneModeChild 					= 0x8017
    SceneModeScene                  = 0x8018
    ColorSketch                     = 0x8019
