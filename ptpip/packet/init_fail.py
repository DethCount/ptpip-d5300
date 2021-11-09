import struct

from .packet import PtpIpPacket

class PtpIpInitFail(PtpIpPacket):
    """docstring for PtpIpInitCmd"""
    def __init__(self, data=None):
        super(PtpIpInitFail, self).__init__()
        self.cmdtype = struct.pack('I', 0x05)
