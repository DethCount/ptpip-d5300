import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader

class CancelTransaction(Packet):
    def __init__(
        self,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None
    ):
        super(CancelTransaction, self).__init__(
            11,
            transactionId = transactionId,
            data = data,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        if data is not None:
            self.transactionId = StreamReader(data=data).readInt32()

    def __str__(self):
        return 'CancelTransaction: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n"
