from ptpip.event_type import EventType

class PtpIpEvent(object):
    def __init__(self, event_type, event_parameter):
        super(PtpIpEvent, self).__init__()
        self.event_type = int(event_type)
        self.event_parameter = int(event_parameter)
