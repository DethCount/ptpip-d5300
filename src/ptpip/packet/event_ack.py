import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet

class EventAck(Packet):
    def __init__(
        self,
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        request: Packet = None,
        sessionId = None
    ):
        super(EventAck, self).__init__(
            4,
            data = data,
            transactionId = transactionId,
            dataObject = dataObject,
            dataObjectTransferMode = dataObjectTransferMode
        )

        self.request = request
        self.sessionId = sessionId

    def __str__(self):
        return 'EventAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n"
