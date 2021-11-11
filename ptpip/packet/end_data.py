import struct

from .packet import PtpIpPacket

class PtpIpEndDataPacket(PtpIpPacket):
    """docstring for Start_Data_Packet"""
    def __init__(self, data=None):
        self.cmdtype = struct.pack('I', 0x12)
        super(PtpIpEndDataPacket, self).__init__()
        if data is not None:
            self.transaction_id = data[0:4]
            print("transaction_id: " + str(struct.unpack('I', self.transaction_id)[0]))
            self.data = data[4:]

    def __str__(self):
        return 'PtpIpEndDataPacket: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'transaction_id: ' + str(self.transaction_id) + "\n" \
            + "\t" + 'data: ' + str(self.data) + "\n"
