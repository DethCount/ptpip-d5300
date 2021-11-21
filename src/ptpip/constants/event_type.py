from enum import Enum

class EventType(Enum):
    # PTP Event Code 0x4000..0x4FFF
    Undefined                   = 0x4000
    CancelTransaction           = 0x4001
    ObjectAdded                 = 0x4002
    ObjectRemoved               = 0x4003
    StoreAdded                  = 0x4004
    StoreRemoved                = 0x4005
    DevicePropChanged           = 0x4006
    ObjectInfoChanged           = 0x4007
    DeviceInfoChanged           = 0x4008
    RequestObjectTransfer       = 0x4009
    StoreFull                   = 0x400A
    DeviceReset                 = 0x400B
    StorageInfoChanged          = 0x400C
    CaptureComplete             = 0x400D
    UnreportedStatus            = 0x400E

    # Vendor Extension Event Code 0xC000..0xC7FF
    ObjectAddedInSdram          = 0xC101
    CaptureCompleteRecInSdram   = 0xC102
    RecordingInterrupted        = 0xC105

    # MTP Event Code 0xC800..0xC8FF
    ObjectPropChanged           = 0xC801
    ObjectPropDescChanged       = 0xC802
    ObjectReferenceChanged      = 0xC803
