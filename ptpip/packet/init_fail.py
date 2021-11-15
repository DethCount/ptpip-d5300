import struct

from .packet import Packet

class InitFail(Packet):
    def __init__(self, data = None):
        super(InitFail, self).__init__()

        self.cmdtype = 5

    def __str__(self):
        return 'InitFail: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
