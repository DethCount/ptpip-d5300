import asyncio

from ptpip.constants.object_format import ObjectFormat
from ptpip.constants.response_code import ResponseCode

from ptpip.client import PtpIpClient

class GetNumObjectsCommand():
    def __init__(self, storageId, objectFormatId, objectFormatName, handle):
        super(GetNumObjectsCommand, self).__init__()

        self.storageId = storageId
        self.objectFormatId = objectFormatId
        self.objectFormatName = objectFormatName
        self.handle = handle

    async def run(self, client: PtpIpClient):

        objectFormat = self.objectFormatId

        if objectFormat is None \
            and self.objectFormatName in ObjectFormat._value2member_map_ \
        :
            objectFormat = ObjectFormat[self.objectFormatName].value \

        response = await client.getNumObjects(
            self.storageId,
            objectFormatId = objectFormat,
            handle = self.handle
        )

        if response is None:
            raise(Exception('Couldn\'t get the number of objects'))

        if isinstance(response, ResponseCode):
            raise(Exception('Error while fetching the number of objects: ' + response.name))

        print(str(response))
