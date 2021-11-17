import struct

from ptpip.constants.response_code import ResponseCode
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader

class CmdResponse(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        request: Packet = None,
        code = None
    ):
        super(CmdResponse, self).__init__(
            7,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.request = request

        if data is not None:
            reader = StreamReader(data = data)
            code = reader.readUint16()
            self.code = ResponseCode(code) \
                if code in ResponseCode._value2member_map_ \
                else code
            self.transactionId = reader.readUint32()
            self.args = reader.readRest()

            print(str(self))

    def __str__(self):
        return 'CmdResponse: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'code: ' + str(self.code) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'args: ' + str(self.args) + "\n"
