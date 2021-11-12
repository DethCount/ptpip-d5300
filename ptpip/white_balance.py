from enum import Enum

class WhiteBalance(Enum):
	Undefined 		= 0x0000
	Auto 			= 0x0002
	Sunny 			= 0x0004
	Fluorescent 	= 0x0005
	Incandescent 	= 0x0006
	Flash 			= 0x0007

	Cloudy 			= 0x8010
	SunnyShade 		= 0x8011
	Preset 			= 0x8013
