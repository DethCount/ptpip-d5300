import struct

from .packet import PtpIpPacket

class PtpIpDataPacket(PtpIpPacket):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None):
        self.cmdtype = struct.pack('I', 0x10)
        super(PtpIpDataPacket, self).__init__()
        if data is not None:
            self.transaction_id = data[0:4]
            self.data = data[4:]
