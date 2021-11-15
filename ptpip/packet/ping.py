import struct

from .packet import Packet
from .stream_writer import StreamWriter

class Ping(Packet):
    def __init__(self, data = None):
        super(Ping, self).__init__()

        self.cmdtype = 13
        self.data = data

    def data(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .data

    def __str__(self):
        return 'Ping: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
