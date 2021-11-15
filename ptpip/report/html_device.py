from datetime import datetime

from html import escape
from typing import List

from ptpip.constants.property_type_mutation import PropertyTypeMutation

from ptpip.data_object.device_info import DeviceInfo
from ptpip.data_object.device_prop_desc import DevicePropDesc

class HtmlDeviceReportGenerator():
    def __init__(
        self,
        device: DeviceInfo,
        props: List[DevicePropDesc] = [],
        discoveredProps: List[DevicePropDesc] = []
    ):
        super(HtmlDeviceReportGenerator, self).__init__()

        self.device = device
        self.props = props
        self.discoveredProps = discoveredProps

    def generateSupportedOperationsReport(self):
        html = '<ul>'

        for op in self.device.operations:
            html += '<li>' + escape(self.device.operationStr(op)) + '</li>'

        return html + '</ul>'


    def generateSupportedEventsReport(self):
        html = '<ul>'

        for evt in self.device.events:
            html += '<li>' + escape(self.device.eventStr(evt)) + '</li>'

        return html + '</ul>'

    def generateObjectFormatsReport(self, objectFormats):
        html = '<ul>'

        for objf in objectFormats:
            html += '<li>' + escape(self.device.objectFormatStr(objf)) + '</li>'

        return html + '</ul>'

    def generatePropertyReport(self, prop: DevicePropDesc):
        html = '<tr>' \
            + '<td style="vertical-align:top;">' \
                + escape(str(prop.typeId)) \
            + '</td>' \
            + '<td style="vertical-align:top;font-weight:bold;">' \
                + escape(prop.type.name if prop.type != None else '') \
            + '</td>' \
            + '<td>' \
                + escape(
                    prop.propType.name \
                    if prop.propType != None \
                    else prop.propTypeId
                ) \
            + '</td>' \
            + '<td>' + escape(prop.mode.name) + '</td>' \
            + '<td>' \
                + escape(prop.propertyValueStr(prop.defaultValue)) \
            + '</td>' \
            + '<td>' \
                + escape(prop.propertyValueStr(prop.value)) \
            + '</td>' \
            + '<td>' \
                + escape(prop.mutation.name) \
            + '</td>'

        if prop.mutation == PropertyTypeMutation.Range:
            html += '<td>' \
                    + '<table border="1" width="100%">' \
                        + '<thead>' \
                            + '<th>Min</th>' \
                            + '<th>Max</th>' \
                            + '<th>Step</th>' \
                        + '</thead>' \
                        + '<tbody>' \
                            + '<tr>' \
                                + '<td>' \
                                    + escape(
                                        prop.propertyValueStr(prop.minValue)
                                    ) \
                                + '</td>' \
                                + '<td>' \
                                    + escape(
                                        prop.propertyValueStr(prop.maxValue)
                                    ) \
                                + '</td>' \
                                + '<td>' + escape(str(prop.step)) + '</td>' \
                            + '</tr>' \
                        + '</tbody>' \
                    + '</table>' \
                + '</td>'
        elif prop.mutation == PropertyTypeMutation.Enumeration:
            html += '<td>' \
                + '<ul>'

            for value in prop.values:
                html += '<li>' + escape(prop.propertyValueStr(value)) + '</li>'

            html += '</ul>' \
                + '</td>'
        else:
            html += '<td></td>'

        return html + '</tr>'

    def generatePropertiesReport(self, properties: List[DevicePropDesc] = []):
        html = '<table border="1" width="100%">' \
            + '<thead>' \
                + '<th>Id</th>' \
                + '<th>Name</th>' \
                + '<th>Type</th>' \
                + '<th>Mode</th>' \
                + '<th>Default</th>' \
                + '<th>Value</th>' \
                + '<th colspan="2">Boundaries</th>' \
            + '</thead>' \
            + '<tbody>'

        for prop in properties:
            print(prop)
            html += self.generatePropertyReport(prop)

        return html + '</tbody>' \
            + '</table>'

    def generate(self):
        return '<table border="1">' \
            + '<thead><th>Key</th><th>Value</th></thead>' \
            + '<tbody>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Report date</td><td>' \
                    + escape(str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Manufacturer</td><td>' \
                    + escape(str(self.device.manufacturer)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Model</td><td>' \
                + escape(str(self.device.model)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Version</td><td>' \
                    + escape(str(self.device.deviceVersion)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">serialNumber</td><td>' \
                    + escape(str(self.device.serialNumber)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Standard version</td><td>' \
                    + escape(str(self.device.standardVersion)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Vendor extension id</td><td>' \
                    + escape(self.device.vendorExtensionIdStr()) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Vendor extension version</td><td>' \
                    + escape(str(self.device.vendorExtensionVersion)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Vendor extension description</td><td>' \
                    + escape(str(self.device.vendorExtensionDesc)) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Status</td><td>' \
                    + escape(self.device.functionalModeStr()) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Operations</td><td>' \
                    + self.generateSupportedOperationsReport() \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Event types</td><td>' \
                    + self.generateSupportedEventsReport() \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Capture formats</td><td>' \
                    + self.generateObjectFormatsReport(self.device.captureFormats) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Image formats</td><td>' \
                    + self.generateObjectFormatsReport(self.device.imageFormats) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Official properties</td><td>' \
                    + self.generatePropertiesReport(self.props) \
                + '</td></tr>' \
                + '<tr><td style="vertical-align:top;font-weight:bold;">Discovered properties</td><td>' \
                    + self.generatePropertiesReport(self.discoveredProps) \
                + '</td></tr>' \
            + '</tbody>' \
            + '</table>'

