from ptpip.data_object import DataObject
from ptpip.device_property_type import DevicePropertyType
from ptpip.property_type import PropertyType
from ptpip.property_type_mutation import PropertyTypeMutation
from ptpip.read_mode import ReadMode

class DevicePropDesc():
    def __init__(self, packet, data):
        super(DevicePropDesc, self).__init__()

        self.packet = packet
        if data == None:
            return

        pos = 0
        (self.type_id, pos) = DataObject.ParseUint16(data, pos)
        self.type = DevicePropertyType(self.type_id) \
            if self.type_id in DevicePropertyType._value2member_map_ \
            else None

        (self.prop_type_id, pos) = DataObject.ParseUint16(data, pos)
        self.prop_type = PropertyType(self.prop_type_id) \
            if self.prop_type_id in PropertyType._value2member_map_ \
            else None

        (self.mode, pos) = DataObject.ParseUint8(data, pos)
        self.mode = ReadMode(self.mode)

        if self.prop_type == None:
            return

        (self.default_value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
        (self.value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)

        self.mutation = None
        # print(str(self))

        (self.mutation, pos) = DataObject.ParseUint8(data, pos)
        self.mutation = PropertyTypeMutation(self.mutation)

        self.min_value = None
        self.max_value = None
        self.step = None
        self.values = None

        try:
            if self.mutation == PropertyTypeMutation.Range:
                (self.min_value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
                (self.max_value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
                (self.step, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
            elif self.mutation == PropertyTypeMutation.Enumeration:
                (self.values, pos) = DataObject.ParseArray(self.prop_type.name, data, pos, 'Uint16')
        except Exception as e:
            print(str(e))
    def __str__(self):
        sMutation = ''
        if self.mutation == PropertyTypeMutation.Range:
            sMutation = "\t" + 'min_value: ' + str(self.min_value) + "\n" \
                + "\t" + 'max_value: ' + str(self.min_value) + "\n" \
                + "\t" + 'step: ' + str(self.step) + "\n"
        elif self.mutation == PropertyTypeMutation.Enumeration:
            sMutation = "\t" + 'values: ' + str(self.values) + "\n"

        return 'DevicePropDesc: ' + "\n" \
            + "\t" + 'type_id: ' + str(self.type_id) + "\n" \
            + "\t" + 'type: ' + str(self.type) + "\n" \
            + "\t" + 'prop_type_id: ' + str(self.prop_type_id) + "\n" \
            + "\t" + 'prop_type: ' + str(self.prop_type) + "\n" \
            + "\t" + 'mode: ' + str(self.mode.name) + "\n" \
            + "\t" + 'default_value: ' + str(self.default_value) + "\n" \
            + "\t" + 'value: ' + str(self.value) + "\n" \
            + "\t" + 'mutation: ' + str(self.mutation) + "\n" \
            + sMutation
