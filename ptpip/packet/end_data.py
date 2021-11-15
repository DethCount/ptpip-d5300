import struct

from .packet import Packet
from .stream_reader import StreamReader

class EndDataPacket(Packet):
    def __init__(self, data = None, request: Packet = None):
        super(EndDataPacket, self).__init__()

        self.cmdtype = 12
        self.request = request

        if data is not None:
            reader = StreamReader(data = data)
            self.transactionId = reader.readUint32()
            print(
                'transactionId: ' \
                    + str(self.transactionId)
            )

            self.data = reader.data[reader.pos:]

    def __str__(self):
        return 'EndDataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
