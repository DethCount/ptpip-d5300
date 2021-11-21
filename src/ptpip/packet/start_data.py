import struct

from ptpip.constants.packet_type import PacketType
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter

class StartDataPacket(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        request: Packet = None,
        length = None
    ):
        super(StartDataPacket, self).__init__(
            PacketType.StartData,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.request = request
        self.length = length

        if data is not None:
            reader = StreamReader(data = data)
            self.transactionId = reader.readUint32()
            self.length = reader.readUint32()

    def pack(self):
        return StreamWriter() \
            .writeUint32(self.type.value) \
            .writeUint32(self.transactionId) \
            .writeUint32(self.length) \
            .data

    def __str__(self):
        return 'StartDataPacket: ' + "\n" \
            + "\t" + 'type: ' + str(self.type) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n" \
            + "\t" + 'length: ' + str(self.length) + "\n"
