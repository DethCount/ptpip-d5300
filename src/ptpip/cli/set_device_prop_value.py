import asyncio

from ptpip.constants.property_type import PropertyType
from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.data_object.device_prop_desc import DevicePropDesc

from ptpip.client import PtpIpClient

class SetDevicePropValueCommand():
    def __init__(self, name, id, propTypeName, propTypeId, value):
        super(SetDevicePropValueCommand, self).__init__()

        self.name = name
        self.id = id
        self.propTypeName = propTypeName
        self.propTypeId = propTypeId
        self.value = value

    async def run(self, client: PtpIpClient):
        prop = self.id if self.id != None else DevicePropertyType[self.name].value

        propType = None
        if self.propTypeId != None:
            propType = PropertyType(self.propTypeId)
        elif self.propTypeName != None:
            propType = PropertyType[self.propTypeName]
        else:
            propDesc = await client.getDevicePropDesc(
                prop = prop
            )

            if not isinstance(propDesc, DevicePropDesc):
                raise(Exception('Error while fetching prop desc: ' + str(propDesc)))

            propType = propDesc.propType

        if not isinstance(propType, PropertyType):
            raise(Exception('Property type not found'))

        value = self.value
        if propType.name[0:3] == 'Int' \
            or propType.name[0:4] == 'Uint' \
        :
            value = int(self.value)

        response = await client.setDevicePropValue(
            prop = prop,
            propType = propType,
            value = value
        )

        print(str(response))
