from enum import Enum
class CmdType(Enum):
    Undefined                   = 0x1000
    GetDeviceInfo               = 0x1001
    OpenSession                 = 0x1002
    CloseSession                = 0x1003
    GetStorageIDs               = 0x1004
    GetStorageInfo              = 0x1005
    GetNumObjects               = 0x1006
    GetObjectHandles            = 0x1007
    GetObjectInfo               = 0x1008
    GetObject                   = 0x1009
    GetThumb                    = 0x100A
    DeleteObject                = 0x100B
    SendObjectInfo              = 0x100C
    SendObject                  = 0x100D
    InitiateCapture             = 0x100E
    FormatStore                 = 0x100F
    ResetDevice                 = 0x1010
    SelfTest                    = 0x1011
    SetObjectProtection         = 0x1012
    PowerDown                   = 0x1013
    GetDevicePropDesc           = 0x1014
    GetDevicePropValue          = 0x1015
    SetDevicePropValue          = 0x1016
    ResetDevicePropValue        = 0x1017
    TerminateOpenCapture        = 0x1018
    MoveObject                  = 0x1019
    CopyObject                  = 0x101A
    GetPartialObject            = 0x101B
    InitiateOpenCapture         = 0x101C
    StartEnumHandles            = 0x101D
    EnumHandles                 = 0x101E
    StopEnumHandles             = 0x101F
    GetVendorExtensionMapss     = 0x1020
    GetVendorDeviceInfo         = 0x1021
    GetResizedImageObject       = 0x1022
    GetFilesystemManifest       = 0x1023
    GetStreamInfo               = 0x1024
    GetStream                   = 0x1025

    InitiateCaptureRecInSdram   = 0x90C0
    AfDrive                     = 0x90C1
    ChangeCameraMode            = 0x90C2
    DeleteImagesInSdram         = 0x90C3
    GetLargeThumb               = 0x90C4
    GetEvent                    = 0x90C7
    DeviceReady                 = 0x90C8
    SetPreWbData                = 0x90C9
    GetVendorPropCodes          = 0x90CA
    AfAndCaptureRecInSdram      = 0x90CB
    GetPicCtrlData              = 0x90CC
    SetPicCtrlData              = 0x90CD
    DeleteCustomPicCtrl         = 0x90CE
    GetPicCtrlCapability        = 0x90CF

    StartLiveView               = 0x9201
    EndLiveView                 = 0x9202
    GetLiveViewImage            = 0x9203
    MfDrive                     = 0x9204
    ChangeAfArea                = 0x9205
    AfDriveCancel               = 0x9206
    InitiateCaptureRecInMedia   = 0x9207
    GetVendorStorageIDs         = 0x9209
    StartMovieRecInCard         = 0x920A
    EndMovieRec                 = 0x920B
    TerminateCapture            = 0x920C

    GetPartialObjectHighSpeed   = 0x9400
    SetTransferListLock         = 0x9407
    GetTransferList             = 0x9408
    NotifyFileAcquisitionStart  = 0x9409
    NotifyFileAcquisitionEnd    = 0x940A
    GetSpecificSizeObject       = 0x940B

    GetObjectPropsSupported     = 0x9801
    GetObjectPropDesc           = 0x9802
    GetObjectPropValue          = 0x9803
    GetObjectPropList           = 0x9805

    WlanPowerControl            = 0x99A1
