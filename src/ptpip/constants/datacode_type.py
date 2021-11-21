from enum import Enum

class DatacodeType(Enum):
    Undefined                       = 0x0000
    PTPOperationCode                = 0x1000
    PTPResponseCode                 = 0x2000
    PTPObjectFormatCode             = 0x3000
    PTPEventCode                    = 0x4000
    PTPDevicePropCode               = 0x5000
    ReservedPTP1                    = 0x6000
    ReservedPTP2                    = 0x7000
    Undefined2                      = 0x8000
    VendorExtensionOperationCode    = 0x9000
    MTPOperationCode                = 0x9800
    VendorExtensionResponseCode     = 0xA000
    MTPResponseCode                 = 0xA800
    VendorExtensionObjectFormatCode = 0xB000
    MTPObjectFormatCode             = 0xB800
    VendorExtensionEventCode        = 0xC000
    MTPEventCode                    = 0xC800
    VendorExtensionDevicePropCode   = 0xD000
    MTPDevicePropCode               = 0xD400
    VendorExtensionObjectPropCode   = 0xD800
    MTPObjectPropCode               = 0xDC00
    ReservedPTP3                    = 0xE000
    ReservedPTP4                    = 0xF000
