import asyncio

from ptpip.constants.object_format import ObjectFormat

from ptpip.data_object.object_handle_array import ObjectHandleArray

from ptpip.client import PtpIpClient

class GetObjectHandlesCommand():
    def __init__(
        self,
        storageId,
        objectFormatId,
        objectFormatName,
        parentHandle,
        allStorages,
        allFormats
    ):
        super(GetObjectHandlesCommand, self).__init__()

        self.storageId = storageId
        self.objectFormatId = objectFormatId
        self.objectFormatName = objectFormatName
        self.parentHandle = parentHandle
        self.allStorages = allStorages
        self.allFormats = allFormats

    async def run(self, client: PtpIpClient):
        objectFormat = self.objectFormatId
        if objectFormat is None \
            and self.objectFormatName is not None \
        :
            objectFormat = ObjectFormat[self.objectFormatName].value

        handles = await client.getObjectHandles(
            storageId = self.storageId,
            objectFormatId = objectFormat,
            handle = self.parentHandle,
            allStorages = self.allStorages,
            allFormats = self.allFormats,
        )

        if not isinstance(handles, ObjectHandleArray):
            raise(Exception('Error while fetching object handles: ' + str(handles)))

        for idx in range(0, len(handles.elements)):
            print(str(handles.elements[idx]))
