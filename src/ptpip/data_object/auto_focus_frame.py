from ptpip.packet.stream_reader import StreamReader

class AutoFocusFrame():
	def __init__(self, data):
		super(AutoFocusFrame, self).__init__()

		self.width = None
		self.height = None
		self.centerX = None
		self.centerY = None

		if data is not None:
			reader = StreamReader(data)
			self.width = reader.readUint16()
			self.height = reader.readUint16()
			self.centerX = reader.readUint16()
			self.centerY = reader.readUint16()

	def __str__(self):
		return self.__class__.__name__ + ': ' + "\n" \
			+ "\t" + 'width: ' + str(self.width) + "\n" \
			+ "\t" + 'height: ' + str(self.height) + "\n" \
			+ "\t" + 'centerX: ' + str(self.centerX) + "\n" \
			+ "\t" + 'centerY: ' + str(self.centerY) + "\n"
