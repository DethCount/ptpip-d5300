from enum import Enum
class CmdType(Enum):
    # PTP Operation Code 0x1000..0x1FFF
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

    # Vendor Extension Operation Code 0x9000..0x97FF

    GetProfileAllData           = 0x9006
    SendProfileData             = 0x9007
    DeleteProfile               = 0x9008
    SetProfileData              = 0x9009
    AdvancedTransfer            = 0x9010
    GetFileInfoInBlock          = 0x9011

    InitiateCaptureRecInSdram   = 0x90C0
    AfDrive                     = 0x90C1
    ChangeCameraMode            = 0x90C2
    DeleteImagesInSdram         = 0x90C3
    GetLargeThumb               = 0x90C4
    GetEvent                    = 0x90C7
    DeviceReady                 = 0x90C8 # 37064
    SetPreWbData                = 0x90C9
    GetVendorPropCodes          = 0x90CA
    AfAndCaptureRecInSdram      = 0x90CB
    GetPicCtrlData              = 0x90CC
    SetPicCtrlData              = 0x90CD
    DeleteCustomPicCtrl         = 0x90CE
    GetPicCtrlCapability        = 0x90CF
    GetDevicePTPIPInfo          = 0x90E0

    GetPreviewImg               = 0x9200
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
    GetFhdPicture               = 0x920F

    GetPartialObjectHighSpeed   = 0x9400
    StartSpotWb                 = 0x9402
    EndSpotWb                   = 0x9403
    ChangeSpotWbArea            = 0x9404
    MeasureSpotWb               = 0x9405
    EndSpotWbResultDisp         = 0x9406
    SetTransferListLock         = 0x9407
    GetTransferList             = 0x9408
    NotifyFileAcquisitionStart  = 0x9409
    NotifyFileAcquisitionEnd    = 0x940A
    GetSpecificSizeObject       = 0x940B
    CancelImagesInSDRAM         = 0x940c
    GetSBHandles                = 0x9414
    GetSBAttrDesc               = 0x9415
    GetSBAttrValue              = 0x9416
    SetSBAttrValue              = 0x9417
    GetSBGroupAttrDesc          = 0x9418
    GetSBGroupAttrValue         = 0x9419
    SetSBGroupAttrValue         = 0x941a
    TestFlash                   = 0x941b
    GetEventEx                  = 0x941c
    MirrorUpCancel              = 0x941d
    PowerZoomByFocalLength      = 0x941e
    ActiveSelectionControl      = 0x941f
    SaveCameraSetting           = 0x9420
    GetObjectSize               = 0x9421
    ChangeMonitorOff            = 0x9422
    GetLiveViewCompressedSize   = 0x9423
    StartTracking               = 0x9424
    EndTracking                 = 0x9425
    ChangeAELock                = 0x9426
    GetLiveViewImageEx          = 0x9428
    GetPartialObjectEx          = 0x9431
    GetManualSettingLensData    = 0x9432
    InitiatePixelMapping        = 0x9433
    GetObjectsMetaData          = 0x9434
    ChangeApplicationMode       = 0x9435
    ResetMenu                   = 0x9436

    GetDevicePropEx             = 0x9504

    # MTP Operation Code 0x9800..0x9FFF
    GetObjectPropsSupported     = 0x9801
    GetObjectPropDesc           = 0x9802
    GetObjectPropValue          = 0x9803
    SetObjectPropValue          = 0x9804
    GetObjectPropList           = 0x9805
    SetObjectPropList           = 0x9806
    GetInterdependendPropdesc   = 0x9807
    SendObjectPropList          = 0x9808
    GetObjectReferences         = 0x9810
    SetObjectReferences         = 0x9811
    UpdateDeviceFirmware        = 0x9812
    Skip                        = 0x9820

    WlanPowerControl            = 0x99A1
