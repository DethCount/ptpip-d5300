from enum import Enum

class ExposureMeteringMode(Enum):
	Undefined 		= 0x0000
	CenterWeighted 	= 0x0002
	MultiPattern 	= 0x0003
	Spot 			= 0x0004
