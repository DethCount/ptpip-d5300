from enum import Enum

class AssociationType(Enum):
	GenericFolder			= 0x0001
	Album					= 0x0002
	TimeSequence			= 0x0003
	HorizontalPanoramic		= 0x0004
	VerticalPanoramic		= 0x0005
	Panoramic2D				= 0x0006
	AncillaryData			= 0x0007
