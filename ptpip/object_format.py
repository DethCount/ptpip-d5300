from enum import Enum

class ObjectFormat(Enum):
    Any                             = 0x0000

    UndefinedAncilliary             = 0x3000
    Association                     = 0x3001
    Script                          = 0x3002
    Executable                      = 0x3003
    Text                            = 0x3004
    Html                            = 0x3005
    Dpof                            = 0x3006
    Aiff                            = 0x3007
    Wav                             = 0x3008
    Mp3                             = 0x3009
    Avi                             = 0x300A
    Mpeg                            = 0x300B
    Asf                             = 0x300C
    Qt                              = 0x300D

    UndefinedImage                  = 0x3800
    ExifJpeg                        = 0x3801
    TiffEp                          = 0x3802
    Flashpix                        = 0x3803
    Bmp                             = 0x3804
    Ciff                            = 0x3805
    Gif                             = 0x3807
    Jfif                            = 0x3808
    Pcd                             = 0x3809
    Pict                            = 0x380A
    Png                             = 0x380B
    Tiff                            = 0x380D
    TiffIt                          = 0x380E
    Jp2                             = 0x380F
    Jpx                             = 0x3810
    Dng                             = 0x3811
    Heif                            = 0x3812

    NetworkAssociation              = 0xB102
    RAW                             = 0xb101

    M4a                             = 0xB215
    Artist                          = 0xB218

    UndefinedFirmware               = 0xB800
    UndefinedFirmwareAndroid        = 0xB802
    WindowsImageFormat              = 0xB881

    UndefinedAudio                  = 0xB900
    Wma                             = 0xB901
    Ogg                             = 0xB902
    Aac                             = 0xB903
    Audible                         = 0xB904
    Flac                            = 0xB906

    UndefinedVideo                  = 0xB980
    Wmv                             = 0xB981
    Mp4                             = 0xB982
    Mp2                             = 0xB983
    _3gp                            = 0xB984

    UndefinedCollection             = 0xBA00
    AbstractMultimediaAlbum         = 0xBA01
    AbstractImageAlbum              = 0xBA02
    AbstractAudioAlbum              = 0xBA03
    AbstractVideoAlbum              = 0xBA04
    AbstractAVPlaylist              = 0xBA05
    AbstractContactGroup            = 0xBA06
    AbstractMessageFolder           = 0xBA07
    AbstractChapteredProduction     = 0xBA08
    AbstractAudioPlaylist           = 0xBA09
    AbstractVideoPlaylist           = 0xBA0a
    AbstractMediacast               = 0xBA0b
    WplPlaylist                     = 0xBA10
    M3uPlaylist                     = 0xBA11
    MplPlaylist                     = 0xBA12
    AsxPlaylist                     = 0xBA13
    PlsPlaylist                     = 0xBA14

    UndefinedDocument               = 0xBA80
    AbstractDocument                = 0xBA81
    XmlDocument                     = 0xBA82
    MicrosoftWordDocument           = 0xBA83
    MhtCompiledHtmlDocument         = 0xBA84
    MicrosoftExcelSpreadsheet       = 0xBA85
    MicrosoftPowerPointPresentation = 0xBA86

    UndefinedMessage                = 0xBB00
    AbstractMessage                 = 0xBB01
    UndefinedContact                = 0xBB80
    AbstractContact                 = 0xBB81
    VCard2                          = 0xBB82
    VCard3                          = 0xBB83

    UndefinedCalendarItem           = 0xBE00
    AbstractCalendarItem            = 0xBE01
    VCalendar1                      = 0xBE02
    VCalendar2                      = 0xBE03
    UndefinedWindowsExecutable      = 0xBE80
