import asyncio
import sys
import time

from ptpip.constants.response_code import ResponseCode

from ptpip.data_object.live_view_object import LiveViewObject

from ptpip.client import PtpIpClient

class GetLiveViewImageCommand():
    def __init__(self, filepath, fps):
        super(GetLiveViewImageCommand, self).__init__()

        self.filepath = filepath
        self.delay = None

        if fps is not None and fps > 0:
            self.delay = 1 / fps

    async def run(self, client: PtpIpClient):
        response = await client.startLiveView()
        if not isinstance(response, ResponseCode):
            raise(Exception('Error while starting live view'))

        if response != ResponseCode.OK:
            raise(Exception('Error while starting live view: ' + str(response)))

        try:
            while not await self.doRun(client) or self.delay:
                time.sleep(self.delay if self.delay else 0.1)
        except KeyboardInterrupt:
            pass
        except Exception as err:
            print('Error during live view: ' + str(err))

        await client.endLiveView()

    async def doRun(self, client: PtpIpClient):
        imgData = await client.getLiveViewImage()

        if isinstance(imgData, ResponseCode):
            if imgData == ResponseCode.DeviceBusy:
                return False
            raise(Exception('Error during live view: ' + str(imgData)))
        if not isinstance(imgData, LiveViewObject):
            raise(Exception('Error during live view'))

        # @todo use LiveViewImage meta

        if self.filepath is not None:
            f = open(self.filepath, 'wb')
            f.write(imgData.content)
            f.close()

            if not self.delay:
                print('Image saved in ' + str(self.filepath))
        else:
            sys.stdout.buffer.write(imgData)

        return True
