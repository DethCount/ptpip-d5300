import struct

from .packet import Packet

class CancelTransaction(Packet):
    def __init__(self, data = None):
        super(CancelTransaction, self).__init__()

        self.cmdtype = struct.pack('I', 0x11)
        if data is not None:
            self.transaction_id = data[0:4]

    def __str__(self):
        return 'CancelTransaction: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n"
