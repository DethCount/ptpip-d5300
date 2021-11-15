import socket
import struct
import uuid

from .packet import Packet
from .stream_reader import StreamReader
from .stream_writer import StreamWriter

class InitCmdReq(Packet):
    def __init__(self, data = None):
        super(InitCmdReq, self).__init__()

        self.cmdtype = 1

        if data is None:
            self.guid = uuid.uuid4().bytes
            self.hostname = socket.gethostname() + '\x00'
            self.hostname = self.hostname.encode()
        else:
            reader = StreamReader(data = data)
            self.guid = reader.readBytes(16)
            self.hostname = reader.readString()

    def data(self):
        return StreamWriter() \
            .writeUint32(self.cmdtype) \
            .writeBytes(self.guid) \
            .writeBytes(self.hostname) \
            .data

    def __str__(self):
        return 'InitCmdReq: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'guid: ' + str(self.guid) + "\n" \
            + "\t" + 'hostname: ' + str(self.hostname) + "\n"
