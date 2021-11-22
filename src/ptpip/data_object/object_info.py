from ptpip.constants.object_format import ObjectFormat
from ptpip.constants.on_off_property import OnOffProperty
from ptpip.constants.object.image_bit_depth import ImageBitDepth
from ptpip.constants.association_type import AssociationType

from ptpip.data_object.storage_info import StorageInfo

from ptpip.packet.stream_reader import StreamReader

class ObjectInfo():
	def __init__(self, packet, data):
		super(ObjectInfo, self).__init__()

		self.packet = packet

		if data is not None:
			reader = StreamReader(data)
			self.storageId = reader.readUint32()
			self.objectFormatId = reader.readUint16()
			self.objectFormat = ObjectFormat(self.objectFormatId) \
				if self.objectFormatId in ObjectFormat._value2member_map_ \
				else None
			self.protectionStatusId = reader.readUint16()
			self.protectionStatus = OnOffProperty(self.protectionStatusId) \
				if self.protectionStatusId in OnOffProperty._value2member_map_ \
				else None
			self.compressedSize = reader.readUint32()
			self.thumbFormatId = reader.readUint16()
			self.thumbFormat = ObjectFormat(self.thumbFormatId) \
				if self.thumbFormatId in ObjectFormat._value2member_map_ \
				else None
			self.thumbCompressedSize = reader.readUint32()
			self.thumbPixWidth = reader.readUint32()
			self.thumbPixHeight = reader.readUint32()
			self.imagePixWidth = reader.readUint32()
			self.imagePixHeight = reader.readUint32()
			self.imageBitDepthId = reader.readUint32()
			self.imageBitDepth = ImageBitDepth(self.imageBitDepthId) \
				if self.imageBitDepthId in ImageBitDepth._value2member_map_ \
				else None
			self.parentObjectHandle = reader.readUint32()
			self.associationTypeId = reader.readUint16()
			self.associationType = AssociationType(self.associationTypeId) \
				if self.associationTypeId in AssociationType._value2member_map_ \
				else None
			self.associationDesc = reader.readUint32()
			self.sequenceNumber = reader.readUint32()
			self.filename = reader.readString()
			self.captureDate = reader.readString()
			self.modificationDate = reader.readString()
			self.keywords = reader.readUint8()

	def __str__(self):
		return self.__class__.__name__ + ': ' + "\n" \
			+ "\t" + 'storageId: ' + str(self.storageId) + "\n" \
			+ "\t" + 'objectFormatId: ' + str(self.objectFormatId) + "\n" \
			+ "\t" + 'objectFormat: ' + (
				self.objectFormat.name \
				if self.objectFormat is not None \
				else ''
			) + "\n" \
			+ "\t" + 'protectionStatusId: ' + str(self.protectionStatusId) + "\n" \
			+ "\t" + 'protectionStatus: ' + (
				self.protectionStatus.name \
				if self.protectionStatus is not None \
				else ''
			) + "\n" \
			+ "\t" + 'compressedSize: ' + StorageInfo.sizeof(self.compressedSize) + "\n" \
			+ "\t" + 'thumbPixWidth: ' + str(self.thumbPixWidth) + "\n" \
			+ "\t" + 'thumbPixHeight: ' + str(self.thumbPixHeight) + "\n" \
			+ "\t" + 'imagePixWidth: ' + str(self.imagePixWidth) + "\n" \
			+ "\t" + 'imagePixHeight: ' + str(self.imagePixHeight) + "\n" \
			+ "\t" + 'imageBitDepthId: ' + str(self.imageBitDepthId) + "\n" \
			+ "\t" + 'imageBitDepth: ' + (
				self.imageBitDepth.name \
				if self.imageBitDepth is not None \
				else ''
			) + "\n" \
			+ "\t" + 'parentObjectHandle: ' + str(self.parentObjectHandle) + "\n" \
			+ "\t" + 'associationTypeId: ' + str(self.associationTypeId) + "\n" \
			+ "\t" + 'associationType: ' + (
				self.associationType.name \
				if self.associationType is not None \
				else ''
			) + "\n" \
			+ "\t" + 'associationDesc: ' + str(self.associationDesc) + "\n" \
			+ "\t" + 'sequenceNumber: ' + str(self.sequenceNumber) + "\n" \
			+ "\t" + 'filename: ' + self.filename + "\n" \
			+ "\t" + 'captureDate: ' + self.captureDate + "\n" \
			+ "\t" + 'modificationDate: ' + self.modificationDate + "\n" \
			+ "\t" + 'keywords: ' + str(self.keywords) + "\n"
