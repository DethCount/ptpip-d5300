from enum import Enum

class FlashMode(Enum):
	Prohibited = 0x0002
	RedEyeReduction = 0x0004

	FrontCurtainSync = 0x8010
	SlowSync = 0x8011
	RearCurtainSync = 0x8012
	RedEyeReductionSlowSync = 0x8013
