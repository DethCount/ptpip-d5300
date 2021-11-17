import socket
import struct
import uuid

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter

class InitCmdReq(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None
    ):
        super(InitCmdReq, self).__init__(
            1,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        if data is None:
            self.guid = uuid.uuid4().bytes
            self.hostname = socket.gethostname() + '\x00'
            self.hostname = self.hostname.encode()
        else:
            reader = StreamReader(data = data)
            self.guid = reader.readBytes(16)
            self.hostname = reader.readString()

    def pack(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeBytes(self.guid) \
            .writeBytes(self.hostname) \
            .data

    def __str__(self):
        return 'InitCmdReq: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'guid: ' + str(self.guid) + "\n" \
            + "\t" + 'hostname: ' + str(self.hostname) + "\n"
