import struct

from .packet import Packet

class EventAck(Packet):
    """docstring for InitCmd"""
    def __init__(self, data=None):
        super(EventAck, self).__init__()
        self.cmdtype = struct.pack('I', 0x04)

    def __str__(self):
        return 'EventAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
