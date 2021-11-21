import asyncio

from ptpip.client import PtpIpClient

from ptpip.report.html_device import HtmlDeviceReportGenerator

class GetDeviceInfoCommand():
    def __init__(self, discover, discoverMore, reportFileName):
        super(GetDeviceInfoCommand, self).__init__()

        self.discover = discover
        self.discoverMore = discoverMore
        self.reportFileName = reportFileName

    async def run(self, client: PtpIpClient):
        device = await client.getDeviceInfo()
        # print('Device: ' + str(device))

        props = []
        for idx, prop in enumerate(device.properties):
            propDesc = await client.getDevicePropDesc(
                prop = prop,
                delay = 0
            )
            props.append(propDesc)
            # print('Prop desc(' + str(idx) + '):' + "\n" + str(propDesc))

        discoveredProps = []
        if self.discover:
            discoveredProps = await client.discoverDevicePropDesc(
                device,
                delay = 0.001 if self.discoverMore else 0.010,
                more = self.discoverMore
            )

        # print(str(discoveredProps))

        html = HtmlDeviceReportGenerator(device, props, discoveredProps) \
            .generate()

        f = open(self.reportFileName, 'w')
        f.write(html)
        f.close()

        print('Report saved ! ' + self.reportFileName)
