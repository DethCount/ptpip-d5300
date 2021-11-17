import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter

class EndDataPacket(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        request: Packet = None
    ):
        super(EndDataPacket, self).__init__(
            12,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.request = request

        if data is not None:
            reader = StreamReader(data = data)
            self.transactionId = reader.readUint32()
            self.data = reader.readRest()
        else:
            self.transactionId = transactionId

    def pack(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeUint32(self.transactionId) \
            .data

    def __str__(self):
        return 'EndDataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
