import struct

from .packet import Packet

class InitCmdAck(Packet):
    def __init__(self, data = None):
        super(InitCmdAck, self).__init__()

        self.cmdtype = struct.pack('I', 0x02)
        if data is not None:
            self.session_id = data[0:4]
            self.guid = data[4:20]
            self.hostname = data[20:]

    def __str__(self):
        return 'InitCmdAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'session_id: ' + str(self.session_id) + "\n" \
            + "\t" + 'guid: ' + str(self.guid) + "\n" \
            + "\t" + 'hostname: ' + str(self.hostname) + "\n"
