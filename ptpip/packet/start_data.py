import struct

from .packet import Packet

class StartDataPacket(Packet):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None, request: Packet = None):
        super(StartDataPacket, self).__init__()

        self.cmdtype = struct.pack('I', 0x09)
        self.request = request

        if data is not None:
            self.transaction_id = data[0:4]
            self.length = data[4:8]

    def __str__(self):
        return 'StartDataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n" \
            + "\t" + 'length: ' + str(self.length) + "\n"
