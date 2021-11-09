import struct

from .packet import PtpIpPacket

class PtpIpInitCmdAck(PtpIpPacket):
    """docstring for PtpIpInitCmd"""
    def __init__(self, data=None):
        super(PtpIpInitCmdAck, self).__init__()
        self.cmdtype = struct.pack('I', 0x02)
        if data is not None:
            self.session_id = data[0:4]
            self.guid = data[4:20]
            self.hostname = data[20:]
