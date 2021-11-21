from enum import Enum

class LiveViewProhibitionCondition(Enum):
    RecordingToSDCard = 1
    SequenceError = 2
    FullyPressedButtonError = 8
    ApertureValueSetByLensApertureRing = 16
    BulbError = 32
    DuringMirrorUpOperation = 64
    DuringInsufficiencyOfBattery = 128
    TTLError = 256
    WhileApertureValueOperationByLensApertureRingIsValid = 512
    NonCPULensMountedAndExposureModeIsNotManual = 1024
