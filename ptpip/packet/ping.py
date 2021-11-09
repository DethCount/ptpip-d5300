import struct

from .packet import PtpIpPacket

class PtpIpPing(PtpIpPacket):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None):
        self.cmdtype = struct.pack('I', 0x13)
        super(PtpIpPing, self).__init__()
        if data is not None:
            self.data = ''

    def data(self):
        return self.cmdtype
