from ptpip.cmd_type import CmdType
from ptpip.event_type import EventType
from ptpip.device_property_type import DevicePropertyType
from ptpip.functional_mode import FunctionalMode
from ptpip.object_format import ObjectFormat
from ptpip.vendor_extension import VendorExtension

from .data_object import PtpIpDataObject

class DeviceInfo(object):
    def __init__(self, data):
        super(DeviceInfo, self).__init__()

        (self.standardVersion, pos) = PtpIpDataObject.ParseUint16(data, 0)
        (self.vendorExtensionId, pos) = PtpIpDataObject.ParseUint32(data, pos)
        (self.vendorExtensionVersion, pos) = PtpIpDataObject.ParseUint16(data, pos)
        (self.vendorExtensionDesc, pos) = PtpIpDataObject.ParseString(data, pos)
        (self.functionalMode, pos) = PtpIpDataObject.ParseUint16(data, pos)
        (self.operationsSupported, pos) = PtpIpDataObject.ParseArray('Uint16', data, pos)
        (self.eventsSupported, pos) = PtpIpDataObject.ParseArray('Uint16', data, pos)
        (self.devicePropertiesSupported, pos) = PtpIpDataObject.ParseArray('Uint16', data, pos)
        (self.captureFormats, pos) = PtpIpDataObject.ParseArray('Uint16', data, pos)
        (self.imageFormats, pos) = PtpIpDataObject.ParseArray('Uint16', data, pos)
        (self.manufacturer, pos) = PtpIpDataObject.ParseString(data, pos)
        (self.model, pos) = PtpIpDataObject.ParseString(data, pos)
        (self.deviceVersion, pos) = PtpIpDataObject.ParseString(data, pos)
        (self.serialNumber, pos) = PtpIpDataObject.ParseString(data, pos)

    def __str__(self):

        print(str(12288 in ObjectFormat._value2member_map_))
        print(str(0x3000 in ObjectFormat._value2member_map_))
        sOperationsSupported = "[\n"
        for i in range(0, len(self.operationsSupported)):
            sOp = CmdType(self.operationsSupported[i]).name \
                if self.operationsSupported[i] in CmdType._value2member_map_ \
                else str(self.operationsSupported[i])

            sOperationsSupported += "\t" + sOp + ",\n"
        sOperationsSupported += "]"

        sEventsSupported = "[\n"
        for i in range(0, len(self.eventsSupported)):
            sEvt = EventType(self.eventsSupported[i]).name \
                if self.eventsSupported[i] in EventType._value2member_map_ \
                else str(self.eventsSupported[i])

            sEventsSupported += "\t" + sEvt + ",\n"
        sEventsSupported += "]"

        sDevicePropertiesSupported = "[\n"
        for i in range(0, len(self.devicePropertiesSupported)):
            sProp = DevicePropertyType(self.devicePropertiesSupported[i]).name \
                if self.devicePropertiesSupported[i] in DevicePropertyType._value2member_map_ \
                else str(self.devicePropertiesSupported[i])

            sDevicePropertiesSupported += "\t" + sProp + ",\n"
        sDevicePropertiesSupported += "]"

        sCaptureFormats = "[\n"
        for i in range(0, len(self.captureFormats)):
            sCap = ObjectFormat(self.captureFormats[i]).name \
                if self.captureFormats[i] in ObjectFormat._value2member_map_ \
                else str(self.captureFormats[i])

            sCaptureFormats += "\t" + sCap + ",\n"
        sCaptureFormats += "]"

        sImageFormats = "[\n"
        for i in range(0, len(self.imageFormats)):
            sImg = ObjectFormat(self.imageFormats[i]).name \
                if self.imageFormats[i] in ObjectFormat._value2member_map_ \
                else str(self.imageFormats[i])

            sImageFormats += "\t" + sImg + ",\n"
        sImageFormats += "]"

        sVendorExtensionId = VendorExtension(self.vendorExtensionId).name \
            if self.vendorExtensionId in VendorExtension._value2member_map_ \
            else str(self.vendorExtensionId)

        sFunctionalMode = FunctionalMode(self.functionalMode).name \
            if self.functionalMode in FunctionalMode._value2member_map_ \
            else str(self.functionalMode)

        return '---- DeviceInfo ----' + "\n" \
            + 'standardVersion: ' + str(self.standardVersion) + "\n" \
            + 'vendorExtensionId: ' + sVendorExtensionId + "\n" \
            + 'vendorExtensionVersion: ' + str(self.vendorExtensionVersion) + "\n" \
            + 'vendorExtensionDesc: ' + str(self.vendorExtensionDesc) + "\n" \
            + 'functionalMode: ' + sFunctionalMode + "\n" \
            + 'operationsSupported: ' + sOperationsSupported + "\n" \
            + 'eventsSupported: ' + sEventsSupported + "\n" \
            + 'devicePropertiesSupported: ' + sDevicePropertiesSupported + "\n" \
            + 'captureFormats: ' + sCaptureFormats + "\n" \
            + 'imageFormats: ' + sImageFormats + "\n" \
            + 'manufacturer: ' + str(self.manufacturer) + "\n" \
            + 'model: ' + str(self.model) + "\n" \
            + 'deviceVersion: ' + str(self.deviceVersion) + "\n" \
            + 'serialNumber: ' + str(self.serialNumber) + "\n" \
            + '---- End DeviceInfo ----'
