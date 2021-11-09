import struct

from ptpip.cmd_type import CmdType
from ptpip.packet import PtpIpPacket

class PtpIpCmdRequest(PtpIpPacket):
    def __init__(
        self,
        transaction_id=None,
        data=None,
        cmd=None,
        param1=None,
        param2=None,
        param3=None,
        param4=None,
        param5=None
    ):
        super(PtpIpCmdRequest, self).__init__()
        self.cmdtype = struct.pack('I', 0x06)
        self.unkown = struct.pack('I', 0x01)
        self.ptp_cmd = cmd
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5
        # Todo: Transaction ID generieren
        self.transaction_id = struct.pack('I', transaction_id)
        self.args = b''
        if self.param1 is not None:
            self.args = self.args + struct.pack('I', self.param1)

        if self.param2 is not None:
            self.args = self.args + struct.pack('I', self.param2)

        if self.param3 is not None:
            self.args = self.args + struct.pack('I', self.param3)

        if self.param4 is not None:
            self.args = self.args + struct.pack('I', self.param4)

        if self.param5 is not None:
            self.args = self.args + struct.pack('I', self.param5)

    def data(self):
        return self.cmdtype \
            + self.unkown \
            + struct.pack('H', self.ptp_cmd) \
            + self.transaction_id \
            + self.args
