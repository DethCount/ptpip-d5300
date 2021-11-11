import struct

from ptpip.response_code import ResponseCode

from .packet import PtpIpPacket

class PtpIpCmdResponse(PtpIpPacket):
    def __init__(self, data=None):
        super(PtpIpCmdResponse, self).__init__()
        self.cmdtype = struct.pack('I', 0x07)
        if data is not None:
            self.ptp_response_code = struct.unpack('H', data[0:2])[0]
            self.transaction_id = data[2:6]
            self.args = data[6:]

    def __str__(self):
        return 'PtpIpCmdResponse: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'ptp_response_code: ' + str(self.ptp_response_code) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n" \
            + "\t" + 'args: ' + str(self.args) + "\n"
