import asyncio

from ptpip.data_object.storage_info import StorageInfo

from ptpip.client import PtpIpClient

class GetStorageInfoCommand():
    def __init__(self, storageId):
        super(GetStorageInfoCommand, self).__init__()

        self.storageId = storageId

    async def run(self, client: PtpIpClient):
        storage = await client.getStorageInfo(self.storageId)

        if not isinstance(storage, StorageInfo):
            raise(Exception('Error while fetching storage info: ' + str(storage)))

        print(str(storage))
