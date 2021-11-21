import asyncio
import sys

from PIL import Image

sys.path.append('./src')

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.event_type import EventType
from ptpip.constants.property_type import PropertyType
from ptpip.constants.response_code import ResponseCode

from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.exposure_ev_step import ExposureEVStep
from ptpip.constants.device.exposure_index import ExposureIndex
from ptpip.constants.device.exposure_program_mode import ExposureProgramMode
from ptpip.constants.device.exposure_time import ExposureTime
from ptpip.constants.device.image_size import ImageSize
from ptpip.constants.device.recording_media import RecordingMedia
from ptpip.constants.device.scene_mode import SceneMode
from ptpip.constants.device.white_balance import WhiteBalance

from ptpip.client import PtpIpClient
from ptpip.packet.cmd_request import CmdRequest
from ptpip.packet.cmd_response import CmdResponse

from ptpip.report.html_device import HtmlDeviceReportGenerator

astronomyMode = (
    {
        "prop": DevicePropertyType.WhiteBalance.value,
        "propType": PropertyType.Uint16,
        "value": WhiteBalance.Incandescent.value
    },
    {
        "prop": DevicePropertyType.ExposureEVStep.value,
        "propType": PropertyType.Uint8,
        "value": ExposureEVStep.ThirdEV.value
    },
)

astronomyGuidingMode = astronomyMode + (
    {
        "prop": DevicePropertyType.ImageSize.value,
        "propType": PropertyType.String,
        "value": ImageSize.Pix2992x2000.value
    },
    {
        "prop": DevicePropertyType.ExposureIndex.value,
        "propType": PropertyType.Uint16,
        "value": ExposureIndex.Iso3200.value
    },
    {
        "prop": DevicePropertyType.ExposureTime.value,
        "propType": PropertyType.Uint32,
        "value": ExposureTime.OneOver4000.value
    },
    {
        "prop": DevicePropertyType.RecordingMedia.value,
        "propType": PropertyType.Uint8,
        "value": RecordingMedia.SDRAM.value
    }
)

astronomyLongExposureMode = astronomyMode + (
    {
        "prop": DevicePropertyType.ImageSize.value,
        "propType": PropertyType.String,
        "value": ImageSize.Pix6000x4000.value
    },
    {
        "prop": DevicePropertyType.ExposureIndex.value,
        "propType": PropertyType.Uint16,
        "value": ExposureIndex.Hi1.value
    },
    {
        "prop": DevicePropertyType.ExposureTime.value,
        "propType": PropertyType.Uint32,
        "value": ExposureTime.OneBy30.value
    },
    {
        "prop": DevicePropertyType.RecordingMedia.value,
        "propType": PropertyType.Uint8,
        "value": RecordingMedia.SDCard.value
    }
)

async def switchMode(client: PtpIpClient, mode: list):
    for setPropArgs in mode:
        propName = DevicePropertyType(setPropArgs['prop']).name \
            if setPropArgs['prop'] in DevicePropertyType._value2member_map_ \
            else setPropArgs['prop']

        print(
            propName + '(' + PropertyType(setPropArgs['propType']).name + '): ' \
                + str(setPropArgs['value'])
        )

        response = await client.setDevicePropValue(
            prop=setPropArgs['prop'],
            propType = setPropArgs['propType'],
            value=setPropArgs['value']
        )

        if not isinstance(response, ResponseCode):
            raise(Exception('Error while setting property ' + propName))

        if response != ResponseCode.OK:
            raise(Exception('Error while setting property ' + propName \
                + ': ' + response.name
            ))

async def usePtpIpClient(client: PtpIpClient):
    await switchMode(client, astronomyGuidingMode)

PtpIpClient(
    usePtpIpClient,
    communicationThreadDelay = 0,
    debug = True
)
