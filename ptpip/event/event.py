from ptpip.constants.event_type import EventType

class Event(object):
    def __init__(self, event_type, event_parameter):
        super(Event, self).__init__()
        self.event_type = int(event_type)
        self.event_parameter = int(event_parameter)
