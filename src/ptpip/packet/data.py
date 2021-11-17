import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter

class DataPacket(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        request: Packet = None,
        content = None
    ):
        super(DataPacket, self).__init__(
            10,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.request = request
        self.content = content

        if data is not None:
            reader = StreamReader(data)
            self.transactionId = reader.readUint32()
            self.content = reader.readRest()

    def pack(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeUint32(self.transactionId) \
            .writeBytes(self.content) \
            .data

    def __str__(self):
        return 'DataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
