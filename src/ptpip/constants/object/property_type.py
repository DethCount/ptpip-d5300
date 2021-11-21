from enum import Enum

class ObjectPropertyType(Enum):
    Undefined                           = 0x0000 # 0

    StorageID                           = 0xDC01 # 56321
    ObjectFormat                        = 0xDC02 # 56322 @see ObjectFormat
    ProtectionStatus                    = 0xDC03 # 56323 @see OnOffProperty
    ObjectSize                          = 0xDC04 # 56324
    ObjectFilename                      = 0xDC07 # 56327
    DateCreated                         = 0xDC08 # 56328
    DateModified                        = 0xDC09 # 56329
    ParentObject                        = 0xDC0B # 56331
    PersistentUniqueObjectIdentifier    = 0xDC41 # 56385
    Name                                = 0xDC44 # 56388

    RepresentativeSampleFormat          = 0xDC81 # 56449 @see ObjectFormat
    RepresentativeSampleSize            = 0xDC82 # 56450
    RepresentativeSampleHeight          = 0xDC83 # 56451
    RepresentativeSampleWidth           = 0xDC84 # 56452
    RepresentativeSampleData            = 0xDC86 # 56454
    Width                               = 0xDC87 # 56455
    Height                              = 0xDC88 # 56456
    ImageBitDepth                       = 0xDCD3 # 56531 @see ImageBitDepth
    Duration                            = 0xDC89 # 56457

    SampleRate                          = 0xDE93 # 56979 @see SampleRate
    NumberOfChannels                    = 0xDE94 # 56980 @see NumberOfChannels
    ScanType                            = 0xDE97 # 56983 @see ScanType
    AudioBitRate                        = 0xDE9A # 56986
    VideoFourCCCode                     = 0xDE9B # 56987 @see VideoFourCCCode
    VideoBitRate                        = 0xDE9C # 56988
    FramesPerMilliseconds               = 0xDE9D
    KeyframeDistance                    = 0xDE9E
    BufferSize                          = 0xDE9F
    EncodingQuality                     = 0xDEA0
    EncodingProfile                     = 0xDEA1

    DisplayName                         = 0xDCE0
    BodyText                            = 0xDCE1
    Subject                             = 0xDCE2
    Priority                            = 0xDCE3

    Owner                               = 0xDD5D
    Editor                              = 0xDD5E
    WebMaster                           = 0xDD5F
    UrlSource                           = 0xDD60
    UrlDestination                      = 0xDD61
    TimeBookmark                        = 0xDD62
    ObjectBookmark                      = 0xDD63
    ByteBookmark                        = 0xDD64

    LastBuildDate                       = 0xDD70
    TimeToLive                          = 0xDD71
    MediaGUID                           = 0xDD72
