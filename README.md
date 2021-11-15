# Getting started

```
import asyncio

from ptpip.client import PtpIpClient
from ptpip.report.html_device import HtmlDeviceReportGenerator

async def usePtpIpClient(client: PtpIpClient):
    device = await client.get_device_info()
    props = []
    for idx, prop in enumerate(device.properties):
        prop_desc = await client.get_device_prop_desc(
            prop=prop,
            transaction_id=0x100 | idx,
            delay=0
        )
        props.append(prop_desc)

    discoveredProps = await client.discover_device_prop_desc(device, delay=0)

    html = HtmlDeviceReportGenerator(device, props, discoveredProps) \
        .generate()

    reportFileName = 'd5300.html'
    f = open(reportFileName, 'w')
    f.write(html)
    f.close()

    print('Report saved ! ' + reportFileName)

PtpIpClient(usePtpIpClient)

```

[Sample report for Nikon d5300](https://dethcount.github.io/ptpip-d5300/d5300.html)

# References

https://github.com/mmattes/ptpip \
http://www.gphoto.org/doc/ptpip.php \
https://github.com/Fimagena/libptp \
https://github.com/whoozle/android-file-transfer-linux/tree/master/mtp/ptp \
https://github.com/Parrot-Developers/sequoia-ptpy/blob/master/ptpy/ptp.py
https://api.ricoh/docs/theta-web-api/property/still_capture_mode/ \
\
https://manualzz.com/download/46005016 D5000 MTP Specifications \
https://www.usb.org/sites/default/files/MTPv1_1.zip \
https://github.com/gphoto/libgphoto2/
