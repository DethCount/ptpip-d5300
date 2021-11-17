import asyncio

from PIL import Image

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.event_type import EventType
from ptpip.constants.property_type import PropertyType

from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.exposure_time import ExposureTime

from ptpip.client import PtpIpClient
from ptpip.packet.cmd_request import CmdRequest

from ptpip.report.html_device import HtmlDeviceReportGenerator

async def usePtpIpClient(client: PtpIpClient):
    device = await client.getDeviceInfo()
    # print('Device: ' + str(device))

    props = []
    for idx, prop in enumerate(device.properties):
        propDesc = await client.getDevicePropDesc(
            prop = prop,
            delay = 0
        )
        props.append(propDesc)
        # print('Prop desc(' + str(idx) + '):' + "\n" + str(propDesc))

    discoveredProps = await client.discoverDevicePropDesc(device, delay = 0.010)
    # print(str(discoveredProps))

    html = HtmlDeviceReportGenerator(device, props, discoveredProps) \
        .generate()

    reportFileName = 'd5300.html'
    f = open(reportFileName, 'w')
    f.write(html)
    f.close()

    print('Report saved ! ' + reportFileName)

    setExposureIndexResponse = await client.setDevicePropValue(
        prop = DevicePropertyType.ExposureIndex.value,
        propType = PropertyType.Uint16,
        value = 3200
    )

    print('setExposureIndexResponse: ' + str(setExposureIndexResponse))

    exposureIndex = await client.getDevicePropValue(
        prop = DevicePropertyType.ExposureIndex.value,
        propType = PropertyType.Uint16
    )

    print('Exposure index : ' + str(exposureIndex))

    """
    pictureControlCapabilities = await client.getPictureControlCapabilities()
    """

    """

    client.setDevicePropDesc(
        prop = DevicePropertyType.ExposureTime.value,
        value = ExposureTime.OneOver4000.value
    )
    """

    """
    # create a PTP/IP command request object and add it to the queue of the PTP/IP connection object
    cmd = CmdRequest(
        transactionId = 2,
        cmd = CmdType.InitiateCaptureRecInMedia.value,
        param1 = 0xffffffff,
        param2 = 0x0000
    )
    packet = client.sendCmd(cmd)

    # get the events from the camera, they will be stored in the eventQueue of the ptpip object
    cmd = CmdRequest(
        cmd = CmdType.GetEvent.value
    )
    packet = client.sendCmd(cmd)

    # query the events for the event you are looking for, for example the 0x4002 ObjectAdded if you look
    # for a image captured
    for event in client.conn.eventQueue:
        if event.eventType == EventType.ObjectAdded.value:
            cmd = CmdRequest(
                cmd = CmdType.GetObject.value,
                param1 = event.parameter
            )
            packet = client.sendCmd(cmd)
    """

PtpIpClient(usePtpIpClient)
