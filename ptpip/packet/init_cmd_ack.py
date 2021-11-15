import struct

from .packet import Packet
from .stream_reader import StreamReader

class InitCmdAck(Packet):
    def __init__(self, data = None):
        super(InitCmdAck, self).__init__()

        self.cmdtype = 2
        if data is not None:
            reader = StreamReader(data = data)
            self.sessionId = reader.readUint32()
            self.guid = reader.readBytes(16)
            self.hostname = reader.readRest()

    def __str__(self):
        return 'InitCmdAck: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'sessionId: ' + str(self.sessionId) + "\n" \
            + "\t" + 'guid: ' + str(self.guid) + "\n" \
            + "\t" + 'hostname: ' + str(self.hostname) + "\n"
