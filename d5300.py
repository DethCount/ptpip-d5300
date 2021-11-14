import asyncio

from PIL import Image

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.event_type import EventType

from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.exposure_time import ExposureTime

from ptpip.client import PtpIpClient
from ptpip.packet.cmd_request import CmdRequest

from ptpip.report.html_device import HtmlDeviceReportGenerator

async def usePtpIpClient(client: PtpIpClient):
    # create a PTP/IP command request device info and add it to the queue of the PTP/IP connection object
    # ptpip_cmd = CmdRequest(transaction_id=1, cmd=CmdType.GetDeviceInfo.value)
    # ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

    device = await client.get_device_info()
    # print('Device: ' + str(device))

    props = []
    for idx, prop in enumerate(device.properties):
        prop_desc = await client.get_device_prop_desc(
            prop=prop,
            transaction_id=0x100 | idx,
            delay=0
        )
        props.append(prop_desc)
            # print('Prop desc(' + str(idx) + '):' + "\n" + str(prop_desc))

    discoveredProps = await client.discover_device_prop_desc(device, delay=0)
    # print(str(discoveredProps))

    html = HtmlDeviceReportGenerator(device, props, discoveredProps) \
        .generate()

    reportFileName = 'd5300.html'
    f = open(reportFileName, 'w')
    f.write(html)
    f.close()

    print('Report saved ! ' + reportFileName)

    """
    picture_control_capabilities = await conn.get_picture_control_capabilities(
        transaction_id = 0xFFF
    )
    """

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

    """
    # create a PTP/IP command request object and add it to the queue of the PTP/IP connection object
    ptpip_cmd = CmdRequest(
        transaction_id = 2,
        cmd=CmdType.InitiateCaptureRecInMedia.value,
        param1 = 0xffffffff,
        param2 = 0x0000
    )
    ptpip_packet = conn.send_cmd(ptpip_cmd)

    # get the events from the camera, they will be stored in the event_queue of the ptpip object
    ptpip_cmd = CmdRequest(
        transaction_id=3,
        cmd=CmdType.GetEvent.value
    )
    ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

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

PtpIpClient(usePtpIpClient)
