import struct

from .packet import Packet

class InitFail(Packet):
    """docstring for InitCmd"""
    def __init__(self, data=None):
        super(InitFail, self).__init__()
        self.cmdtype = struct.pack('I', 0x05)

    def __str__(self):
        return 'InitFail: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
