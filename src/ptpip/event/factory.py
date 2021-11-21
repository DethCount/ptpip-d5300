import struct

from ptpip.event.event import Event

from ptpip.packet.stream_reader import StreamReader

class EventFactory():
    """
    This is a factory to produce an array of Event objects if it got passd a data reply
    from a GetEvent request 0x90C7
    """
    def __init__(self, data):
        super(EventFactory, self).__init__()
        self.events = []

        reader = StreamReader(data)

        nbEvents = reader.readUint16()

        counter = 1
        for idx in range(0, nbEvents):

            self.events.append(Event(
                reader.readUint16(),
                reader.readUint32()
            ))

    def getEvents(self):
        return self.events
