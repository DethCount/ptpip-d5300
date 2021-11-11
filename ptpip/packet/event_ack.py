import struct

from .packet import PtpIpPacket

class PtpIpEventAck(PtpIpPacket):
    """docstring for PtpIpInitCmd"""
    def __init__(self, data=None):
        super(PtpIpEventAck, self).__init__()
        self.cmdtype = struct.pack('I', 0x04)

    def __str__(self):
        return 'PtpIpEventAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
