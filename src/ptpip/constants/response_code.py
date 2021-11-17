from enum import Enum

class ResponseCode(Enum):
    Undefined                                = 0x2000
    OK                                       = 0x2001
    GeneralError                             = 0x2002
    SessionNotOpen                           = 0x2003
    InvalidTransactionID                     = 0x2004
    OperationNotSupported                    = 0x2005
    ParameterNotSupported                    = 0x2006
    IncompleteTransfer                       = 0x2007
    InvalidStorageID                         = 0x2008
    InvalidObjectHandle                      = 0x2009
    DevicePropNotSupported                   = 0x200A
    InvalidObjectFormatCode                  = 0x200B
    StoreFull                                = 0x200C
    ObjectWriteProtected                     = 0x200D
    StoreReadOnly                            = 0x200E
    AccessDenied                             = 0x200F
    NoThumbnailPresent                       = 0x2010
    SelfTestFailed                           = 0x2011
    PartialDeletion                          = 0x2012
    StoreNotAvailable                        = 0x2013
    SpecificationByFormatUnsupported         = 0x2014
    NoValidObjectInfo                        = 0x2015
    InvalidCodeFormat                        = 0x2016
    UnknownVendorCode                        = 0x2017
    CaptureAlreadyTerminated                 = 0x2018
    DeviceBusy                               = 0x2019
    InvalidParentObject                      = 0x201A
    InvalidDevicePropFormat                  = 0x201B
    InvalidDevicePropValue                   = 0x201C
    InvalidParameter                         = 0x201D
    SessionAlreadyOpen                       = 0x201E
    TransactionCancelled                     = 0x201F
    SpecificationOfDestinationUnsupported    = 0x2020
    InvalidEnumHandle                        = 0x2021
    NoStreamEnabled                          = 0x2022
    InvalidDataset                           = 0x2023

    NIKON_HardwareError                      = 0xA001
    NIKON_OutOfFocus                         = 0xA002
    NIKON_ChangeCameraModeFailed             = 0xA003
    NIKON_InvalidStatus                      = 0xA004
    NIKON_SetPropertyNotSupport              = 0xA005
    NIKON_WbPresetError                      = 0xA006
    NIKON_DustReferenceError                 = 0xA007
    NIKON_ShutterSpeedBulb                   = 0xA008
    NIKON_MirrorUpSequence                   = 0xA009
    NIKON_CameraModeNotAdjustFnumber         = 0xA00A
    NIKON_NotLiveView                        = 0xA00B
    NIKON_MfDriveStepEnd                     = 0xA00C
    NIKON_MfDriveStepInsufficiency           = 0xA00E
    NIKON_AdvancedTransferCancel             = 0xA022
    NIKON_UnknownError                       = 0xA081

    NIKON_Bulb_Release_Busy                  = 0xA200
    NIKON_Silent_Release_Busy                = 0xA201
    NIKON_MovieFrame_Release_Busy            = 0xA202
    NIKON_ShutterSpeed_Time                  = 0xA204
    NIKON_Waiting2ndRelease                  = 0xA207
    NIKON_MirrorUpCaptureAlreadyStart        = 0xA208
    NIKON_InvalidSBAttributeValue            = 0xA209

    MTP_Undefined                            = 0xA800
    MTP_InvalidObjectPropCode                = 0xA801
    MTP_InvalidObjectPropFormat              = 0xA802
    MTP_InvalidObjectPropValue               = 0xA803
    MTP_InvalidObjectReference               = 0xA804
    MTP_InvalidDataset                       = 0xA806
    MTP_SpecificationByGroupUnsupported      = 0xA807
    MTP_SpecificationByDepthUnsupported      = 0xA808
    MTP_ObjectTooLarge                       = 0xA809
    MTP_ObjectPropNotSupported               = 0xA80A

    MTP_InvalidMediaSessionID                = 0xA170
    MTP_MediaSessionLimitReached             = 0xA171
    MTP_NoMoreData                           = 0xA172

    MTP_InvalidWFCSyntax                     = 0xA121
    MTP_WFCVersionNotSupported               = 0xA122


