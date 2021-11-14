import struct

from .packet import Packet

class EventAck(Packet):
    def __init__(self, data = None, request: Packet = None):
        super(EventAck, self).__init__()

        self.cmdtype = struct.pack('I', 0x04)
        self.request = request

    def __str__(self):
        return 'EventAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
