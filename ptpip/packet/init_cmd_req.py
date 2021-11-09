import socket
import struct
import uuid

from .packet import PtpIpPacket

class PtpIpInitCmdReq(PtpIpPacket):
    """docstring for PtpIpInitCmd"""
    def __init__(self, data=None):
        super(PtpIpInitCmdReq, self).__init__()
        self.cmdtype = struct.pack('I', 0x01)
        if data is None:
            guid = uuid.uuid4()
            self.guid = guid.bytes
            self.hostname = socket.gethostname() + '\x00'
            self.hostname = self.hostname.encode()
        else:
            self.guid = data[0:16]
            self.hostname = data[16:0]

    def data(self):
        return self.cmdtype + self.guid + self.hostname
