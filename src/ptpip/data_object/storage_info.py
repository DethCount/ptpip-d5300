from ptpip.constants.storage.access_capability import AccessCapability
from ptpip.constants.storage.type import StorageType
from ptpip.constants.storage.filesystem_type import FilesystemType

from ptpip.packet.stream_reader import StreamReader

class StorageInfo():
	def __init__(self, packet, data):
		super(StorageInfo, self).__init__()

		self.packet = packet

		if data is not None:
			reader = StreamReader(data)
			self.typeId = reader.readUint16()
			self.type = StorageType(self.typeId) \
				if self.typeId in StorageType._value2member_map_ \
				else None

			self.filesystemTypeId = reader.readUint16()
			self.filesystemType = FilesystemType(self.filesystemTypeId) \
				if self.filesystemTypeId in FilesystemType._value2member_map_ \
				else None

			self.accessCapabilityId = reader.readUint16()
			self.accessCapability = AccessCapability(self.accessCapabilityId) \
				if self.accessCapabilityId in AccessCapability._value2member_map_ \
				else None

			self.maxCapacity = reader.readUint64()
			self.freeSpaceInBytes = reader.readUint64()
			self.freeSpaceInImages = reader.readUint32()
			self.description = reader.readUint8()
			self.volumeLabel = reader.readString()

	def sizeof(num, suffix = "B"):
		for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
			if abs(num) < 1024.0:
				return f"{num:3.1f}{unit}{suffix}"
			num /= 1024.0

		return f"{num:.1f}Yi{suffix}"

	def __str__(self):
		return 'StorageInfo: ' + "\n" \
			+ "\t" + 'typeId: ' + str(self.typeId) + "\n" \
			+ "\t" + 'type: ' + (
				self.type.name \
				if self.type is not None \
				else ''
			) + "\n" \
			+ "\t" + 'filesystemTypeId: ' + str(self.filesystemTypeId) + "\n" \
			+ "\t" + 'filesystemType: ' + (
				self.filesystemType.name \
				if self.filesystemType is not None \
				else ''
			) + "\n" \
			+ "\t" + 'accessCapabilityId: ' + str(self.accessCapabilityId) + "\n" \
			+ "\t" + 'accessCapability: ' + (
				self.accessCapability.name \
					if self.accessCapability is not None \
					else ''
			) + "\n" \
			+ "\t" + 'maxCapacity: ' + StorageInfo.sizeof(self.maxCapacity) + "\n" \
			+ "\t" + 'freeSpaceInBytes: ' + StorageInfo.sizeof(self.freeSpaceInBytes) + "\n" \
			+ "\t" + 'freeSpaceInImages: ' + str(self.freeSpaceInImages) + "\n" \
			+ "\t" + 'description: ' + str(self.description) + "\n" \
			+ "\t" + 'volumeLabel: ' + str(self.volumeLabel) + "\n"
