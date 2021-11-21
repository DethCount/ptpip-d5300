from ptpip.constants.event_type import EventType

class Event():
    def __init__(self, typeId, parameter):
        super(Event, self).__init__()

        self.typeId = typeId
        self.type = EventType(self.typeId) \
            if self.typeId in EventType._value2member_map_ \
            else None

        self.parameter = parameter

    def __str__(self):
        return 'Event: ' + "\n" \
            + "\t" + 'typeId: ' + str(self.typeId) + "\n" \
            + "\t" + 'type: ' + (self.type.name if self.type != None else '') + "\n" \
            + "\t" + 'parameter: ' + str(self.parameter) + "\n"
