from ptpip.packet.stream_reader import StreamReader

class StorageIdArray():
    def __init__(self, packet, data):
        super(StorageIdArray, self).__init__()

        self.packet = packet
        self.length = 0
        self.elements = []
        self.sdCardInserted = None

        if data is not None:
            reader = StreamReader(data)
            self.length = reader.readUint32()

            for elt in range(0, self.length):
                self.elements.append(reader.readUint32())

            self.sdCardInserted = len(self.elements) > 0 \
                and self.elements[0] == 0x00010001

    def __str__(self):
        sElements = ''
        for idx in range(0, len(self.elements)):
            sElements += "\t\t" + str(self.elements[idx]) + "\n"

        return 'StorageIdArray:' + "\n" \
            + "\t" + 'length: ' + str(self.length) + "\n" \
            + "\t" + 'sdCardInserted: ' + str(self.sdCardInserted) + "\n" \
            + "\t" + 'elements: [' + "\n" \
                + sElements \
            + "\t]\n"
