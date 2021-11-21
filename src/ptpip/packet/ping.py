import struct

from ptpip.constants.packet_type import PacketType
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_writer import StreamWriter

class Ping(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None
    ):
        super(Ping, self).__init__(
            PacketType.Ping,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

    def pack(self):
        return StreamWriter() \
            .writeUint32(self.type.value) \
            .data

    def __str__(self):
        return 'Ping: ' + "\n" \
            + "\t" + 'type: ' + str(self.type) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
