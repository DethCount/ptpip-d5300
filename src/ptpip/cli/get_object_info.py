import asyncio

from ptpip.data_object.object_info import ObjectInfo

from ptpip.client import PtpIpClient

class GetObjectInfoCommand():
    def __init__(self, handle):
        super(GetObjectInfoCommand, self).__init__()

        self.handle = handle

    async def run(self, client: PtpIpClient):
        objectInfo = await client.getObjectInfo(self.handle)

        if not isinstance(objectInfo, ObjectInfo):
            raise(Exception('Error while fetching object info: ' + str(objectInfo)))

        print(str(objectInfo))
