from enum import Enum

class DevicePropertyType(Enum):
	Undefined 					= 0x5000
	BatteryLevel				= 0x5001
	FunctionalMode				= 0x5002 # @see FunctionalMode
	ImageSize					= 0x5003
	CompressionSetting			= 0x5004
	WhiteBalance				= 0x5005
	RgbGain						= 0x5006
	FNumber 					= 0x5007
	FocalLength 				= 0x5008
	FocusDistance 				= 0x5009
	FocusMode 					= 0x500A
	ExposureMeteringMode		= 0x500B
	FlashMode					= 0x500C
	ExposureTime 				= 0x500D
	ExposureProgramMode 		= 0x500E
	ExposureIndex 				= 0x500F
	ExposureBiasCompensation	= 0x5010
	DateTime 					= 0x5011
	CaptureDelay 				= 0x5012
	StillCaptureMode 			= 0x5013
	Contrast 					= 0x5014
	Sharpness 					= 0x5015
	DigitalZoom 				= 0x5016
	EffectMode 					= 0x5017
	BurstNumber 				= 0x5018
	BurstInterval 				= 0x5019
	TimelapseNumber 			= 0x501A
	TimelapseInterval 			= 0x501B
	FocusMeteringMode 			= 0x501C
	UploadUrl 					= 0x501D
	Artist 						= 0x501E
	CopyrightInfo 				= 0x501F

	AudioVolume 				= 0x502C

	ErrorInfo 					= 0xD006
	ShutterSpeed 				= 0xD00F

	DeviceEUI64					= 0xD210

	SynchronizationPartner		= 0xD401
	DeviceFriendlyName			= 0xD402
	Volume						= 0xD403
	SupportedFormatsOrdered		= 0xD404
	DeviceIcon					= 0xD405
	SessionInitiatorVersionInfo	= 0xD406
	PerceivedDeviceType			= 0xD407
	PlaybackRate				= 0xD410
	PlaybackObject				= 0xD411
	PlaybackContainerIndex		= 0xD412
	PlaybackPosition			= 0xD413

	GpsInfo 					= 0xD801
	AutoPowerOffDelay 			= 0xD802
	SleepDelay 					= 0xD803
	ChannelNumber 				= 0xD807
	CaptureStatus 				= 0xD808
	RecordingTime 				= 0xD809
	RemainingRecordingTime 		= 0xD80A
