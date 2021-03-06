from enum import Enum

class ObjectPropertyType(Enum):
    Undefined                           = 0x0000 # 0

    WirelessConfigurationFile           = 0xB104

    BuyFlag                             = 0xD901

    # MTP Object Prop Code 0xDC00..0xDFFF
    StorageID                           = 0xDC01 # 56321
    ObjectFormat                        = 0xDC02 # 56322 @see ObjectFormat
    ProtectionStatus                    = 0xDC03 # 56323 @see OnOffProperty
    ObjectSize                          = 0xDC04 # 56324
    AssociationType                     = 0xDC05
    AssociationDesc                     = 0xDC06
    ObjectFilename                      = 0xDC07 # 56327
    DateCreated                         = 0xDC08 # 56328
    DateModified                        = 0xDC09 # 56329
    Keywords                            = 0xDC0A
    ParentObject                        = 0xDC0B # 56331
    AllowedFolderContents               = 0xDC0C
    Hidden                              = 0xDC0D
    SystemObject                        = 0xDC0E

    PersistentUniqueObjectIdentifier    = 0xDC41 # 56385
    SyncID                              = 0xDC42
    PropertyBag                         = 0xDC43
    Name                                = 0xDC44 # 56388
    CreatedBy                           = 0xDC45
    Artist                              = 0xDC46
    DateAuthored                        = 0xDC47
    Description                         = 0xDC48
    URLReference                        = 0xDC49
    LanguageLocale                      = 0xDC4A
    CopyrightInformation                = 0xDC4B
    Source                              = 0xDC4C
    OriginLocation                      = 0xDC4D
    DateAdded                           = 0xDC4E
    NonConsumable                       = 0xDC4F
    CorruptOrUnplayable                 = 0xDC50
    ProducerSerialNumber                = 0xDC51

    RepresentativeSampleFormat          = 0xDC81 # 56449 @see ObjectFormat
    RepresentativeSampleSize            = 0xDC82 # 56450
    RepresentativeSampleHeight          = 0xDC83 # 56451
    RepresentativeSampleWidth           = 0xDC84 # 56452
    RepresentativeSampleDuration        = 0xDC85
    RepresentativeSampleData            = 0xDC86 # 56454
    Width                               = 0xDC87 # 56455
    Height                              = 0xDC88 # 56456
    Duration                            = 0xDC89 # 56457
    Rating                              = 0xDC8A
    Track                               = 0xDC8B
    Genre                               = 0xDC8C
    Credits                             = 0xDC8D
    Lyrics                              = 0xDC8E
    SubscriptionContentID               = 0xDC8F
    ProducedBy                          = 0xDC90
    UseCount                            = 0xDC91
    SkipCount                           = 0xDC92
    LastAccessed                        = 0xDC93
    ParentalRating                      = 0xDC94
    MetaGenre                           = 0xDC95
    Composer                            = 0xDC96
    EffectiveRating                     = 0xDC97
    Subtitle                            = 0xDC98
    OriginalReleaseDate                 = 0xDC99
    AlbumName                           = 0xDC9A
    AlbumArtist                         = 0xDC9B
    Mood                                = 0xDC9C
    DRMStatus                           = 0xDC9D
    SubDescription                      = 0xDC9E
    IsCropped                           = 0xDCD1
    IsColorCorrected                    = 0xDCD2
    ImageBitDepth                       = 0xDCD3 # 56531 @see ImageBitDepth
    Fnumber                             = 0xDCD4
    ExposureTime                        = 0xDCD5
    ExposureIndex                       = 0xDCD6
    DisplayName                         = 0xDCE0
    BodyText                            = 0xDCE1
    Subject                             = 0xDCE2
    Priority                            = 0xDCE3
    GivenName                           = 0xDD00
    MiddleNames                         = 0xDD01
    FamilyName                          = 0xDD02
    Prefix                              = 0xDD03
    Suffix                              = 0xDD04
    PhoneticGivenName                   = 0xDD05
    PhoneticFamilyName                  = 0xDD06
    EmailPrimary                        = 0xDD07
    EmailPersonal1                      = 0xDD08
    EmailPersonal2                      = 0xDD09
    EmailBusiness1                      = 0xDD0A
    EmailBusiness2                      = 0xDD0B
    EmailOthers                         = 0xDD0C
    PhoneNumberPrimary                  = 0xDD0D
    PhoneNumberPersonal                 = 0xDD0E
    PhoneNumberPersonal2                = 0xDD0F
    PhoneNumberBusiness                 = 0xDD10
    PhoneNumberBusiness2                = 0xDD11
    PhoneNumberMobile                   = 0xDD12
    PhoneNumberMobile2                  = 0xDD13
    FaxNumberPrimary                    = 0xDD14
    FaxNumberPersonal                   = 0xDD15
    FaxNumberBusiness                   = 0xDD16
    PagerNumber                         = 0xDD17
    PhoneNumberOthers                   = 0xDD18
    PrimaryWebAddress                   = 0xDD19
    PersonalWebAddress                  = 0xDD1A
    BusinessWebAddress                  = 0xDD1B
    InstantMessengerAddress             = 0xDD1C
    InstantMessengerAddress2            = 0xDD1D
    InstantMessengerAddress3            = 0xDD1E
    PostalAddressPersonalFull           = 0xDD1F
    PostalAddressPersonalFullLine1      = 0xDD20
    PostalAddressPersonalFullLine2      = 0xDD21
    PostalAddressPersonalFullCity       = 0xDD22
    PostalAddressPersonalFullRegion     = 0xDD23
    PostalAddressPersonalFullPostalCode = 0xDD24
    PostalAddressPersonalFullCountry    = 0xDD25
    PostalAddressBusinessFull           = 0xDD26
    PostalAddressBusinessLine1          = 0xDD27
    PostalAddressBusinessLine2          = 0xDD28
    PostalAddressBusinessCity           = 0xDD29
    PostalAddressBusinessRegion         = 0xDD2A
    PostalAddressBusinessPostalCode     = 0xDD2B
    PostalAddressBusinessCountry        = 0xDD2C
    PostalAddressOtherFull              = 0xDD2D
    PostalAddressOtherLine1             = 0xDD2E
    PostalAddressOtherLine2             = 0xDD2F
    PostalAddressOtherCity              = 0xDD30
    PostalAddressOtherRegion            = 0xDD31
    PostalAddressOtherPostalCode        = 0xDD32
    PostalAddressOtherCountry           = 0xDD33
    OrganizationName                    = 0xDD34
    PhoneticOrganizationName            = 0xDD35
    Role                                = 0xDD36
    Birthdate                           = 0xDD37
    MessageTo                           = 0xDD40
    MessageCC                           = 0xDD41
    MessageBCC                          = 0xDD42
    MessageRead                         = 0xDD43
    MessageReceivedTime                 = 0xDD44
    MessageSender                       = 0xDD45
    ActivityBeginTime                   = 0xDD50
    ActivityEndTime                     = 0xDD51
    ActivityLocation                    = 0xDD52
    ActivityRequiredAttendees           = 0xDD54
    ActivityOptionalAttendees           = 0xDD55
    ActivityResources                   = 0xDD56
    ActivityAccepted                    = 0xDD57
    Owner                               = 0xDD5D
    Editor                              = 0xDD5E
    Webmaster                           = 0xDD5F
    URLSource                           = 0xDD60
    URLDestination                      = 0xDD61
    TimeBookmark                        = 0xDD62
    ObjectBookmark                      = 0xDD63
    ByteBookmark                        = 0xDD64
    LastBuildDate                       = 0xDD70
    TimetoLive                          = 0xDD71
    MediaGUID                           = 0xDD72

    TotalBitRate                        = 0xDE91
    BitRateType                         = 0xDE92
    SampleRate                          = 0xDE93 # 56979 @see SampleRate
    NumberOfChannels                    = 0xDE94 # 56980 @see NumberOfChannels
    AudioBitDepth                       = 0xDE95
    ScanType                            = 0xDE97 # 56983 @see ScanType

    AudioWAVECodec                      = 0xDE99
    AudioBitRate                        = 0xDE9A # 56986
    VideoFourCCCode                     = 0xDE9B # 56987 @see VideoFourCCCode
    VideoBitRate                        = 0xDE9C # 56988
    FramesPerMilliseconds               = 0xDE9D
    KeyframeDistance                    = 0xDE9E
    BufferSize                          = 0xDE9F
    EncodingQuality                     = 0xDEA0
    EncodingProfile                     = 0xDEA1
