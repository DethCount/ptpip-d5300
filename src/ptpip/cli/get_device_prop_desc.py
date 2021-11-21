import asyncio

from ptpip.constants.device.property_type import DevicePropertyType

from ptpip.client import PtpIpClient

class GetDevicePropDescCommand():
    def __init__(self, name, id):
        super(GetDevicePropDescCommand, self).__init__()

        self.name = name
        self.id = id

    async def run(self, client: PtpIpClient):
        prop = self.id if self.id != None else DevicePropertyType[self.name].value

        propDesc = await client.getDevicePropDesc(
            prop = prop
        )

        print(str(propDesc))
