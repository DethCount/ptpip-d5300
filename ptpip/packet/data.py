import struct

from .packet import Packet
from .stream_reader import StreamReader

class DataPacket(Packet):
    def __init__(self, data = None, request: Packet = None):
        super(DataPacket, self).__init__()

        self.cmdtype = struct.pack('I', 0x10)
        self.request = request

        if data is not None:
            reader = StreamReader(data)
            self.transactionId = reader.readUint32()
            self.data = reader.data[reader.pos:]

    def __str__(self):
        return 'DataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
