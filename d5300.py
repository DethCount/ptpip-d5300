import asyncio
import io
import sys
import struct
import time
from html import escape

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.event_type import EventType

from ptpip.constants.property_type_mutation import PropertyTypeMutation
from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.exposure_time import ExposureTime

from ptpip.connection import Connection
from ptpip.packet.cmd_request import CmdRequest

from PIL import Image
from threading import Thread, get_ident

def generateSupportedOperationsReport(device):
    html = '<ul>'

    for op in device.operations:
        html += '<li>' + escape(device.operationStr(op)) + '</li>'

    return html + '</ul>'


def generateSupportedEventsReport(device):
    html = '<ul>'

    for evt in device.events:
        html += '<li>' + escape(device.eventStr(evt)) + '</li>'

    return html + '</ul>'

def generateObjectFormatsReport(device, objectFormats):
    html = '<ul>'

    for objf in objectFormats:
        html += '<li>' + escape(device.objectFormatStr(objf)) + '</li>'

    return html + '</ul>'

def generatePropertyReport(device, prop):
    html = '<tr>'

    html += '<td style="vertical-align:top;">' + escape(str(prop.type_id)) +'</td>'
    html += '<td style="vertical-align:top;font-weight:bold;">' + escape(prop.type.name if prop.type != None else '') +'</td>'
    html += '<td>' + escape(prop.prop_type.name if prop.prop_type != None else prop.prop_type_id) +'</td>'
    html += '<td>' + escape(prop.mode.name) +'</td>'
    html += '<td>' + escape(prop.propertyValueStr(prop.default_value)) +'</td>'
    html += '<td>' + escape(prop.propertyValueStr(prop.value)) +'</td>'
    html += '<td>' + escape(prop.mutation.name) +'</td>'

    if prop.mutation == PropertyTypeMutation.Range:
        html += '<td>'
        html += '<table border="1" width="100%">'
        html += '<thead><th>Min</th><th>Max</th><th>Step</th></thead>'
        html += '<tbody>'
        html += '<tr><td>' + escape(prop.propertyValueStr(prop.min_value)) + '</td>'
        html += '<td>' + escape(prop.propertyValueStr(prop.max_value)) + '</td>'
        html += '<td>' + escape(str(prop.step)) + '</td>'
        html += '</tr></tbody>'
        html += '</table>'
        html += '</td>'
    elif prop.mutation == PropertyTypeMutation.Enumeration:
        html += '<td>'
        html += '<ul>'
        for value in prop.values:
            html += '<li>' + escape(prop.propertyValueStr(value)) + '</li>'
        html += '</ul>'
        html += '</td>'
    else:
        html += '<td></td>'

    return html + '</tr>'

def generatePropertiesReport(device, properties):
    html = '<table border="1" width="100%">'
    html += '<thead><th>Id</th><th>Name</th><th>Type</th><th>Mode</th><th>Default</th><th>Value</th><th colspan="2">Boundaries</th></thead>'
    html += '<tbody>'

    for prop in properties:
        print(prop)
        html += generatePropertyReport(device, prop)

    html += '</tbody>'
    return html + '</table>'

def generateDeviceReport(device, props, discoveredProps):
    return '<table border="1">' \
        + '<thead><th>Key</th><th>Value</th></thead>' \
        + '<tbody>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Manufacturer</td><td>' \
                + escape(str(device.manufacturer)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Model</td><td>' \
            + escape(str(device.model)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Version</td><td>' \
                + escape(str(device.deviceVersion)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">serialNumber</td><td>' \
                + escape(str(device.serialNumber)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Standard version</td><td>' \
                + escape(str(device.standardVersion)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Vendor extension id</td><td>' \
                + escape(device.vendorExtensionIdStr()) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Vendor extension version</td><td>' \
                + escape(str(device.vendorExtensionVersion)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Vendor extension description</td><td>' \
                + escape(str(device.vendorExtensionDesc)) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Status</td><td>' \
                + escape(device.functionalModeStr()) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Operations</td><td>' \
                + generateSupportedOperationsReport(device) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Event types</td><td>' \
                + generateSupportedEventsReport(device) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Capture formats</td><td>' \
                + generateObjectFormatsReport(device, device.captureFormats) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Image formats</td><td>' \
                + generateObjectFormatsReport(device, device.imageFormats) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Official properties</td><td>' \
                + generatePropertiesReport(device, props) \
            + '</td></tr>' \
            + '<tr><td style="vertical-align:top;font-weight:bold;">Discovered properties</td><td>' \
                + generatePropertiesReport(device, discoveredProps) \
            + '</td></tr>' \
        + '</tbody>' \
        + '</table>'


def setup():
    conn = Connection()

    conn.open()

    thread_comm = Thread(target=conn.communication_thread, args=(0,))
    thread_comm.daemon = True
    thread_comm.start()

    return conn

async def loop(conn):
    print('loop')
    # START
    # open up a PTP/IP connection, default IP and Port is host='192.168.1.1', port=15740

    # Start the Thread which is constantly checking the status of the camera and which is
    # processing new command packages which should be send


    # thread_obj = Thread(target=conn.treat_object_data_queue, args=(conn, 2))
    # thread_obj.daemon = True
    # thread_obj.start()

    # create a PTP/IP command request device info and add it to the queue of the PTP/IP connection object
    # ptpip_cmd = CmdRequest(transaction_id=1, cmd=CmdType.GetDeviceInfo.value)
    # ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

    device = await conn.get_device_info()
    # print('Device: ' + str(device))

    props = []
    for idx, prop in enumerate(device.properties):
        prop_desc = await conn.get_device_prop_desc(
            prop=prop,
            transaction_id=0x100 | idx,
            delay=0
        )
        props.append(prop_desc)
            # print('Prop desc(' + str(idx) + '):' + "\n" + str(prop_desc))

    discoveredProps = await conn.discover_device_prop_desc(device, delay=0)
    print(str(discoveredProps))

    html = generateDeviceReport(device, props, discoveredProps)
    f = open('d5300.html', 'w')
    f.write(html)
    f.close()
    print('Report generated !')


    # picture_control_capabilities = await conn.get_picture_control_capabilities(
    #    transaction_id = 0xFFF
    # )

    """
    conn.set_device_prop_desc(
        prop=DevicePropertyType.ExposureIndex.value,
        value="1600",
        transaction_id=0x1000 | idx
    )

    conn.set_device_prop_desc(
        prop=DevicePropertyType.ExposureTime.value,
        value=ExposureTime.OneOver4000.value,
        transaction_id=0x1000 | idx
    )
    """

event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(loop(setup()))

except KeyboardInterrupt:
    event_loop.stop()
    pass

"""
# create a PTP/IP command request object and add it to the queue of the PTP/IP connection object
ptpip_cmd = CmdRequest(
    transaction_id=2,
    cmd=CmdType.InitiateCaptureRecInMedia.value,
    param1=0xffffffff,
    param2=0x0000
)
ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

# give the thread / connection some time to process the command and thenn close the connection
time.sleep(5)

# get the events from the camera, they will be stored in the event_queue of the ptpip object
ptpip_cmd = CmdRequest(
    transaction_id=3,
    cmd=CmdType.GetEvent.value
)
ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

# give the thread some time to process the events it received from the camera
time.sleep(2)

# query the events for the event you are looking for, for example the 0x4002 ObjectAdded if you look
# for a image captured
for event in conn.event_queue:
    if event.event_type == EventType.ObjectAdded.value:
        ptpip_cmd = CmdRequest(
            transaction_id=4,
            cmd=CmdType.GetObject.value,
            param1=event.event_parameter
        )
        ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)
"""
# give the thread some time to get the object

# conn.treat_object_data_queue(conn=conn, delay=2)

"""
time.sleep(50000000)

sys.exit()
"""
