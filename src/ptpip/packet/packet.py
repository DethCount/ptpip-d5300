import struct

from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

class Packet(object):
    def __init__(
        self,
        cmdtype,
        transactionId = None,
        data = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None
    ):
        super(Packet, self).__init__()

        self.cmdtype = cmdtype
        self.transactionId = transactionId
        self.data = data
        self.dataObject = dataObject
        self.dataObjectTransferMode = dataObjectTransferMode \
            if dataObjectTransferMode != None \
            else DataObjectTransferMode.Receive

    def pack(self):
        pass
