import struct

from .packet import PtpIpPacket

class PtpIpStartDataPacket(PtpIpPacket):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None):
        self.cmdtype = struct.pack('I', 0x09)
        super(PtpIpStartDataPacket, self).__init__()
        if data is not None:
            self.transaction_id = data[0:4]
            self.length = data[4:8]
