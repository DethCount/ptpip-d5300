from ptpip.packet.stream_reader import StreamReader

class Uint16Array():
    def __init__(self, packet, data):
        super(Uint16Array, self).__init__()

        self.packet = packet
        self.length = 0
        self.elements = []

        if data is not None:
            reader = StreamReader(data)
            self.length = reader.readUint32()

            for elt in range(0, self.length):
                self.elements.append(reader.readUint16())

    def __str__(self):
        return self.__class__.__name__ + ':' + "\n" \
            + "\t" + 'length: ' + str(self.length) + "\n" \
            + "\t" + 'elements: ' + str(self.elements) + "\n"
