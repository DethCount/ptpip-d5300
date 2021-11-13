import struct

from .packet import Packet

class DataPacket(Packet):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None, request: Packet = None):
        super(DataPacket, self).__init__()

        self.cmdtype = struct.pack('I', 0x10)
        self.request = request

        if data is not None:
            self.transaction_id = data[0:4]
            self.data = data[4:]

    def __str__(self):
        return 'DataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
