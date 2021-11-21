from ptpip.constants.object_format import ObjectFormat
from ptpip.constants.on_off_property import OnOffProperty
from ptpip.constants.property_type import PropertyType
from ptpip.constants.property_type_mutation import PropertyTypeMutation

from ptpip.constants.object.property_type import ObjectPropertyType

from ptpip.constants.object.image_bit_depth import ImageBitDepth
from ptpip.constants.object.number_of_channels import NumberOfChannels
from ptpip.constants.object.sample_rate import SampleRate
from ptpip.constants.object.scan_type import ScanType
from ptpip.constants.object.video_four_cc_code import VideoFourCCCode

from ptpip.packet.stream_reader import StreamReader

class ObjectPropDesc():
	def __init__(self, packet, data):
		super(self, ObjectPropDesc).__init__()

        self.packet = packet
        if data == None:
            return

        reader = StreamReader(data = data)

        self.typeId = reader.readUint16()
        self.type = ObjectPropertyType(self.typeId) \
            if self.typeId in ObjectPropertyType._value2member_map_ \
            else None

        self.propTypeId = reader.readUint16()
        self.propType = PropertyType(self.propTypeId) \
            if self.propTypeId in PropertyType._value2member_map_ \
            else None

        self.mode = ReadMode(reader.readUint8())

        if self.propType == None:
            return

        self.defaultValue = reader.readType(self.propType.name)
        self.value = reader.readType(self.propType.name)

        self.mutation = PropertyTypeMutation(reader.readUint8())

        self.minValue = None
        self.maxValue = None
        self.step = None
        self.values = None
        self.length = None
        self.maxLength = None

        try:
            if self.mutation == PropertyTypeMutation.Range:
                self.minValue = reader.readType(self.propType.name)
                self.maxValue = reader.readType(self.propType.name)
                self.step = reader.readType(self.propType.name)
            elif self.mutation == PropertyTypeMutation.Enumeration:
                self.values = reader.readArray(
                    self.propType.name,
                    lengthTypeName = PropertyType.Uint16.name
                )
            elif self.mutation == PropertyTypeMutation.Array:
            	self.length = reader.readUint16()
            elif self.mutation == PropertyTypeMutation.ByteString \
            	or self.mutation == PropertyTypeMutation.Text \
            :
            	self.maxLength = reader.readUint16()
        except Exception as e:
            print(str(e))

    def propertyValueStr(self, value):
        if self.type == ObjectPropertyType.ImageBitDepth \
            and value in ImageBitDepth._value2member_map_ \
            :
                return ImageBitDepth(value).name

        if self.type == ObjectPropertyType.NumberOfChannels \
            and value in NumberOfChannels._value2member_map_ \
            :
                return NumberOfChannels(value).name

        if self.type == ObjectPropertyType.ObjectFormat \
            and value in ObjectFormat._value2member_map_ \
            :
                return ObjectFormat(value).name

        if self.type == ObjectPropertyType.SampleRate \
            and value in SampleRate._value2member_map_ \
            :
                return SampleRate(value).name

        if self.type == ObjectPropertyType.ScanType \
            and value in ScanType._value2member_map_ \
            :
                return ScanType(value).name

        if self.type == ObjectPropertyType.VideoFourCCCode \
            and value in VideoFourCCCode._value2member_map_ \
            :
                return VideoFourCCCode(value).name

        if self.type in (
            ObjectPropertyType.ProtectionStatus
        ) and value in OnOffProperty._value2member_map_ \
        :
            return OnOffProperty(value).name

        return str(value)

    def __str__(self):
        sMutation = ''
        if self.mutation == PropertyTypeMutation.Range:
            if self.minValue != 0 and self.maxValue != 0:
                sMutation += "\t" \
                    + 'min_value: ' \
                        + self.propertyValueStr(self.minValue) + "\n" \
                    + "\t" \
                    + 'max_value: ' \
                        + self.propertyValueStr(self.maxValue) + "\n"

            if self.step != 1:
                sMutation += "\t" + 'step: ' + str(self.step) + "\n"
        elif self.mutation == PropertyTypeMutation.Enumeration:
            sValues = []
            for value in self.values:
                sValues.append(self.propertyValueStr(value))

            sMutation = "\t" + 'values: ' + str(sValues) + "\n"
        elif self.mutation == PropertyTypeMutation.Array:
        	sMutation += "\t" \
        		+ 'length: ' + str(self.length) + "\n"
        elif self.mutation == PropertyTypeMutation.ByteString \
        	or self.mutation == PropertyTypeMutation.Text \
        :
        	sMutation += "\t" \
        		+ 'maxLength: ' + str(self.maxLength) + "\n"

        return 'ObjectPropDesc: ' + "\n" \
            + "\t" + 'typeId: ' + str(self.typeId) + "\n" \
            + "\t" + 'type: ' + str(self.type) + "\n" \
            + "\t" + 'propTypeId: ' + str(self.propTypeId) + "\n" \
            + "\t" + 'propType: ' + str(self.propType) + "\n" \
            + "\t" + 'mode: ' + str(self.mode.name) + "\n" \
            + "\t" + 'defaultValue: ' \
                + self.propertyValueStr(self.defaultValue) + "\n" \
            + "\t" + 'value: ' \
                + self.propertyValueStr(self.value) + "\n" \
            + "\t" + 'mutation: ' + str(self.mutation) + "\n" \
            + sMutation
