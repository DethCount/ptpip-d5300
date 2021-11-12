import struct

from .packet import Packet

class CancelTransaction(Packet):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None):
        self.cmdtype = struct.pack('I', 0x11)
        super(CancelTransaction, self).__init__()
        if data is not None:
            self.transaction_id = data[0:4]

    def __str__(self):
        return 'CancelTransaction: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n"
