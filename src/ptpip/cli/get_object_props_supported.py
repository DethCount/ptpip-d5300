import asyncio

from ptpip.constants.object_format import ObjectFormat
from ptpip.constants.object.property_type import ObjectPropertyType

from ptpip.data_object.object_prop_code_array import ObjectPropCodeArray

from ptpip.client import PtpIpClient

class GetObjectPropsSupportedCommand():
    def __init__(self, objectFormatId, objectFormatName, printPropNames):
        super(GetObjectPropsSupportedCommand, self).__init__()

        self.objectFormatId = objectFormatId
        self.objectFormatName = objectFormatName
        self.printPropNames = printPropNames

    async def run(self, client: PtpIpClient):
        objectFormat = self.objectFormatId

        if objectFormat is None \
            and self.objectFormatName is not None \
        :
            objectFormat = ObjectFormat[self.objectFormatName].value

        propCodes = await client.getObjectPropsSupported(objectFormat)

        if not isinstance(propCodes, ObjectPropCodeArray):
            raise(Exception('Error while fetching supported object property codes: ' \
                + str(propCodes)
            ))

        for idx in range(0, len(propCodes.elements)):
            if self.printPropNames \
                and propCodes.elements[idx] in ObjectPropertyType._value2member_map_ \
            :
                print(ObjectPropertyType(propCodes.elements[idx]).name)
                continue

            print(str(propCodes.elements[idx]))
