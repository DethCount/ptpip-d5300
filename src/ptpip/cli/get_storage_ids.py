import asyncio

from ptpip.data_object.storage_id_array import StorageIdArray

from ptpip.client import PtpIpClient

class GetStorageIdsCommand():
    def __init__(self):
        super(GetStorageIdsCommand, self).__init__()

    async def run(self, client: PtpIpClient):
        storageIds = await client.getStorageIds()

        if not isinstance(storageIds, StorageIdArray):
            raise(Exception('Error while fetching storage ids: ' + str(storageIds)))

        for idx in range(0, len(storageIds.elements)):
            print(str(storageIds.elements[idx]))
