import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet

class InitFail(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None
    ):
        super(InitFail, self).__init__(
            5,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

    def __str__(self):
        return 'InitFail: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
