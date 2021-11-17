import struct

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.property_type import PropertyType
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_writer import StreamWriter

class CmdRequest(Packet):
    def __init__(
        self,
        transactionId = None,
        data = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        cmd = None,
        param1 = None,
        param2 = None,
        param3 = None,
        param4 = None,
        param5 = None,
        paramType1: PropertyType = PropertyType.Uint32,
        paramType2: PropertyType = PropertyType.Uint32,
        paramType3: PropertyType = PropertyType.Uint32,
        paramType4: PropertyType = PropertyType.Uint32,
        paramType5: PropertyType = PropertyType.Uint32,
    ):
        super(CmdRequest, self).__init__(
            cmdtype = 6,
            transactionId = transactionId,
            data = data,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.cmd = cmd
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5
        self.paramType1 = paramType1
        self.paramType2 = paramType2
        self.paramType3 = paramType3
        self.paramType4 = paramType4
        self.paramType5 = paramType5

    def pack(self):
        writer = StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeUint32(self.dataObjectTransferMode.value) \
            .writeUint16(self.cmd) \
            .writeUint32(self.transactionId)

        if self.param1 is not None:
            writer.writeType(self.paramType1.name, self.param1)
        if self.param2 is not None:
            writer.writeType(self.paramType2.name, self.param2)
        if self.param3 is not None:
            writer.writeType(self.paramType3.name, self.param3)
        if self.param4 is not None:
            writer.writeType(self.paramType4.name, self.param4)
        if self.param5 is not None:
            writer.writeType(self.paramType5.name, self.param5)

        return writer.data

    def __str__(self):
        return 'CmdRequest: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'dataObjectTransferMode: ' + str(self.dataObjectTransferMode.name) + "\n" \
            + "\t" + 'ptp_cmd: ' + str(self.cmd) + "\n" \
            + "\t" + 'param1: ' + str(self.param1) + "\n" \
            + "\t" + 'param2: ' + str(self.param2) + "\n" \
            + "\t" + 'param3: ' + str(self.param3) + "\n" \
            + "\t" + 'param4: ' + str(self.param4) + "\n" \
            + "\t" + 'param5: ' + str(self.param5) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n"

