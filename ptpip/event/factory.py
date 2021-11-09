import struct

from ptpip.event.event import PtpIpEvent

class PtpIpEventFactory(object):
    """
    This is a factory to produce an array of PtpIpEvent objects if it got passd a data reply
    from a GetEvent request 0x90C7
    """
    def __init__(self, data):
        super(PtpIpEventFactory, self).__init__()
        # create an empty array for the PtpIpEvent object which will be replied
        self.events = []

        # get the amount of events passed from the data passed to the factory
        amount_of_events = struct.unpack('H', data[0:2])[0]

        # set an counter and an offset of 2 as the first two bytes are already processed
        counter = 1
        offset = 2
        while counter <= amount_of_events:
            # get the event_type which consists of two bytes
            event_type = str(struct.unpack('H', data[offset:offset+2])[0])

            # get the event_parameter which consists of 4 bytes
            event_parameter = str(struct.unpack('I', data[offset+2:offset+6])[0])
            self.events.append(PtpIpEvent(event_type, event_parameter))

            # increase the offset by 6 to get to the next event_type and event_parameter pair
            offset = offset + 6
            counter = counter + 1

    def get_events(self):
        return self.events
