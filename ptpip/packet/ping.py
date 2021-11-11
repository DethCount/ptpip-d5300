import struct

from .packet import PtpIpPacket

class PtpIpPing(PtpIpPacket):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None):
        self.cmdtype = struct.pack('I', 0x13)
        super(PtpIpPing, self).__init__()
        self.data = data

    def data(self):
        return self.cmdtype

    def __str__(self):
        return 'PtpIpPing: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
