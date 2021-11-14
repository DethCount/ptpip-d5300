import struct

from .packet import Packet

class Ping(Packet):
    def __init__(self, data = None):
        super(Ping, self).__init__()

        self.cmdtype = struct.pack('I', 0x13)
        self.data = data

    def data(self):
        return self.cmdtype

    def __str__(self):
        return 'Ping: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
