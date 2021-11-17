import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter

class EventReq(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        sessionId = None
    ):
        super(EventReq, self).__init__(
            3,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.sessionId = None

        if data is not None:
            reader = StreamReader(data = data)
            self.sessionId = reader.readUint32()
        elif sessionId is not None:
            self.sessionId = sessionId

    def pack(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeUint32(self.sessionId) \
            .data

    def __str__(self):
        return 'EventReq: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'sessionId: ' + str(self.sessionId) + "\n"
