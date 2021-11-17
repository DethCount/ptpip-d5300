from ptpip.constants.cmd_type import CmdType
from ptpip.constants.event_type import EventType
from ptpip.constants.object_format import ObjectFormat

from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.functional_mode import FunctionalMode
from ptpip.constants.device.vendor_extension import VendorExtension

from ptpip.packet.stream_reader import StreamReader
from ptpip.data_object.data_object import DataObject

class DeviceInfo():
    def __init__(self, packet, data):
        super(DeviceInfo, self).__init__()
        self.packet = packet

        reader = StreamReader(data = data)
        self.standardVersion        = reader.readUint16()
        self.vendorExtensionId      = reader.readUint32()
        self.vendorExtensionVersion = reader.readUint16()
        self.vendorExtensionDesc    = reader.readString()
        self.functionalMode         = reader.readUint16()
        self.operations             = reader.readUint16Array()
        self.events                 = reader.readUint16Array()
        self.properties             = reader.readUint16Array()
        self.captureFormats         = reader.readUint16Array()
        self.imageFormats           = reader.readUint16Array()
        self.manufacturer           = reader.readString()
        self.model                  = reader.readString()
        self.deviceVersion          = reader.readString()
        self.serialNumber           = reader.readString()

    def vendorExtensionIdStr(self):
        return VendorExtension(self.vendorExtensionId).name \
            if self.vendorExtensionId in VendorExtension._value2member_map_ \
            else str(self.vendorExtensionId)

    def functionalModeStr(self):
        return FunctionalMode(self.functionalMode).name \
            if self.functionalMode in FunctionalMode._value2member_map_ \
            else str(self.functionalMode)

    def operationStr(self, operation):
        return CmdType(operation).name \
            if operation in CmdType._value2member_map_ \
            else str(operation)

    def eventStr(self, event):
        return EventType(event).name \
            if event in EventType._value2member_map_ \
            else str(event)

    def objectFormatStr(self, objectFormat):
        return ObjectFormat(objectFormat).name \
            if objectFormat in ObjectFormat._value2member_map_ \
            else str(objectFormat)

    def __str__(self):
        sOps = "[\n"
        for i in range(0, len(self.operations)):
            sOps += "\t" + self.operationStr(self.operations[i]) + ",\n"
        sOps += "]"

        sEvents = "[\n"
        for i in range(0, len(self.events)):
            sEvents += "\t" + self.eventStr(self.events[i]) + ",\n"
        sEvents += "]"

        sProps = "[\n"
        for i in range(0, len(self.properties)):
            sProp = DevicePropertyType(self.properties[i]).name \
                if self.properties[i] in DevicePropertyType._value2member_map_ \
                else str(self.properties[i])

            sProps += "\t" + sProp + ",\n"
        sProps += "]"

        sCaptureFormats = "[\n"
        for i in range(0, len(self.captureFormats)):
            sCaptureFormats += "\t" + self.objectFormatStr(self.captureFormats[i]) + ",\n"
        sCaptureFormats += "]"

        sImageFormats = "[\n"
        for i in range(0, len(self.imageFormats)):
            sImageFormats += "\t" + self.objectFormatStr(self.imageFormats[i]) + ",\n"
        sImageFormats += "]"

        return '---- DeviceInfo ----' + "\n" \
            + 'standardVersion: ' + str(self.standardVersion) + "\n" \
            + 'vendorExtensionId: ' + self.vendorExtensionIdStr() + "\n" \
            + 'vendorExtensionVersion: ' + str(self.vendorExtensionVersion) + "\n" \
            + 'vendorExtensionDesc: ' + str(self.vendorExtensionDesc) + "\n" \
            + 'functionalMode: ' + self.functionalModeStr() + "\n" \
            + 'operationsSupported: ' + sOps + "\n" \
            + 'eventsSupported: ' + sEvents + "\n" \
            + 'devicePropertiesSupported: ' + sProps + "\n" \
            + 'captureFormats: ' + sCaptureFormats + "\n" \
            + 'imageFormats: ' + sImageFormats + "\n" \
            + 'manufacturer: ' + str(self.manufacturer) + "\n" \
            + 'model: ' + str(self.model) + "\n" \
            + 'deviceVersion: ' + str(self.deviceVersion) + "\n" \
            + 'serialNumber: ' + str(self.serialNumber) + "\n" \
            + '---- End DeviceInfo ----'
