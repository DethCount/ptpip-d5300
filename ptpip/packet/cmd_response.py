import struct

from ptpip.constants.response_code import ResponseCode

from .packet import Packet
from .stream_reader import StreamReader

class CmdResponse(Packet):
    def __init__(self, data = None, request: Packet = None):
        super(CmdResponse, self).__init__()

        self.cmdtype = 7
        self.request = request
        if data is not None:
            reader = StreamReader(data = data)
            code = reader.readUint16()
            self.responseCode = ResponseCode(code) if code in ResponseCode._value2member_map_ else code
            self.transactionId = reader.readUint32()
            self.args = reader.readRest()

            print(str(self))

    def __str__(self):
        return 'CmdResponse: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'responseCode: ' + str(self.responseCode) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'args: ' + str(self.args) + "\n"
