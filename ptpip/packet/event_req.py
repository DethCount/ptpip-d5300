import struct

from .packet import Packet

class EventReq(Packet):
    """docstring for InitCmd"""
    def __init__(self, data=None, session_id=None):
        super(EventReq, self).__init__()
        self.cmdtype = struct.pack('I', 0x03)
        self.session_id = None
        if data is not None:
            self.session_id = data[0:4]
        elif session_id is not None:
            self.session_id = session_id

    def data(self):
        return self.cmdtype + self.session_id

    def __str__(self):
        return 'EventReq: ' + "\n" \
            + "\t" + 'cmdtype: ' + str(self.cmdtype) + "\n" \
            + "\t" + 'session_id: ' + str(self.session_id) + "\n"
