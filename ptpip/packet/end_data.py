import struct

from .packet import Packet

class EndDataPacket(Packet):
    def __init__(self, data = None, request: Packet = None):
        super(EndDataPacket, self).__init__()

        self.cmdtype = struct.pack('I', 0x12)
        self.request = request

        if data is not None:
            self.transaction_id = data[0:4]
            print("transaction_id: " + str(struct.unpack('I', self.transaction_id)[0]))
            self.data = data[4:]

    def __str__(self):
        return 'EndDataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
