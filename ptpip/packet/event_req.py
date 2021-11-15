import struct

from .packet import Packet
from .stream_reader import StreamReader
from .stream_writer import StreamWriter

class EventReq(Packet):
    def __init__(self, data = None, sessionId = None):
        super(EventReq, self).__init__()

        self.cmdtype = 3
        self.sessionId = None

        if data is not None:
            reader = StreamReader(data = data)
            self.sessionId = reader.readUint32()
        elif sessionId is not None:
            self.sessionId = sessionId

    def data(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeUint32(self.sessionId) \
            .data

    def __str__(self):
        return 'EventReq: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'sessionId: ' + str(self.sessionId) + "\n"
