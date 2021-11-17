import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader

class InitCmdAck(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        sessionId = None
    ):
        super(InitCmdAck, self).__init__(
            2,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.sessionId = sessionId
        self.guid = None
        self.hostname = None

        if data is not None:
            reader = StreamReader(data = data)
            self.sessionId = reader.readUint32()
            self.guid = reader.readBytes(16)
            self.hostname = reader.readRest()

    def __str__(self):
        return 'InitCmdAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'sessionId: ' + str(self.sessionId) + "\n" \
            + "\t" + 'guid: ' + str(self.guid) + "\n" \
            + "\t" + 'hostname: ' + str(self.hostname) + "\n"
