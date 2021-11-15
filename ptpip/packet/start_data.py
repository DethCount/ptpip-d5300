import struct

from .packet import Packet
from .stream_reader import StreamReader

class StartDataPacket(Packet):
    def __init__(self, data = None, request: Packet = None):
        super(StartDataPacket, self).__init__()

        self.cmdtype = 9
        self.request = request

        if data is not None:
            reader = StreamReader(data = data)
            self.transactionId = reader.readUint32()
            self.length = reader.readUint32()

    def __str__(self):
        return 'StartDataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'length: ' + str(self.length) + "\n"
