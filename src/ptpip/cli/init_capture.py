import asyncio
import sys

from ptpip.client import PtpIpClient

class InitCaptureCommand():
    def __init__(self, filepath):
        super(InitCaptureCommand, self).__init__()

        self.filepath = filepath

    async def run(self, client: PtpIpClient):
        imgData = await client.initCapture()

        if self.filepath is not None:
            f = open(self.filepath, 'wb')
            f.write(imgData)
            f.close()
            print('Image saved in ' + str(self.filepath))
        else:
            sys.stdout.buffer.write(imgData)
