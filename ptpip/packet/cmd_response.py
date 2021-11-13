import struct

from ptpip.constants.response_code import ResponseCode

from .packet import Packet

class CmdResponse(Packet):
    def __init__(self, data=None, request: Packet = None):
        super(CmdResponse, self).__init__()
        self.cmdtype = struct.pack('I', 0x07)
        self.request = request
        if data is not None:
            self.ptp_response_code = ResponseCode(struct.unpack('H', data[0:2])[0])
            self.transaction_id = data[2:6]
            self.args = data[6:]

    def __str__(self):
        return 'CmdResponse: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'ptp_response_code: ' + str(self.ptp_response_code) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n" \
            + "\t" + 'args: ' + str(self.args) + "\n"
