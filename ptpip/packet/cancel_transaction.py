import struct

from .packet import Packet
from .stream_reader import StreamReader

class CancelTransaction(Packet):
    def __init__(self, data = None):
        super(CancelTransaction, self).__init__()

        self.cmdtype = 11
        if data is not None:
            self.transactionId = StreamReader(data=data).readInt32()

    def __str__(self):
        return 'CancelTransaction: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transactionId: ' + str(self.transactionId) + "\n"
