import struct

from .packet import PtpIpPacket

class PtpIpEventReq(PtpIpPacket):
    """docstring for PtpIpInitCmd"""
    def __init__(self, data=None, session_id=None):
        super(PtpIpEventReq, self).__init__()
        self.cmdtype = struct.pack('I', 0x03)
        self.session_id = None
        if data is not None:
            self.session_id = data[0:4]
        elif session_id is not None:
            self.session_id = session_id

    def data(self):
        return self.cmdtype + self.session_id
