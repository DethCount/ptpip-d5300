from ptpip.constants.event_type import EventType

class Event():
    def __init__(self, event_type, parameter):
        super(Event, self).__init__()

        self.type = int(event_type)
        self.parameter = int(parameter)
