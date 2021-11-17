import struct

class DataObject():
    def __init__(
        self,
        packet = None,
        data = None
    ):
        super(DataObject, self).__init__()

        self.packet = packet
        self.data = data

    def __str__(self):
        return 'DataObject: ' + "\n" \
            + "\t" + 'Packet: ' + str(self.packet) + "\n" \
            + "\t" + 'Data: ' + str(self.data) + "\n"
