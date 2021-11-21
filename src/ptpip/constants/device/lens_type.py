from enum import Enum

class LensType(Enum):
    Undefined                                   = 0
    DTypeLenWithDistanceEncoder                 = 1
    VRLensWithAntiVibrationMechanism            = 2
    DXLensExclusiveUseOfNikon                   = 4
    AFSLens                                     = 8
    LensSupportingAutomaticDistortionCorrection = 16
    Unknown1                                    = 32
    Unknown2                                    = 64
