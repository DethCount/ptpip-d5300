# Getting started

[pip package](https://pypi.org/project/ptpip/)

```
pip install ptpip
```

[d5300 sample file](https://github.com/DethCount/ptpip-d5300/blob/master/d5300.py)

```
from ptpip.client import PtpIpClient
from ptpip.report.html_device import HtmlDeviceReportGenerator

async def usePtpIpClient(client: PtpIpClient):
    device = await client.getDeviceInfo()
    props = []
    for idx, prop in enumerate(device.properties):
        prop_desc = await client.getDevicePropDesc(
            prop=prop,
            delay=0
        )
        props.append(prop_desc)

    discoveredProps = await client.discoverDevicePropDesc(device, delay=0)

    html = HtmlDeviceReportGenerator(device, props, discoveredProps) \
        .generate()

    reportFileName = 'd5300.html'
    f = open(reportFileName, 'w')
    f.write(html)
    f.close()

    print('Report saved ! ' + reportFileName)

    setExposureIndexResponse = await client.setDevicePropValue(
        prop = DevicePropertyType.ExposureIndex.value,
        propType = PropertyType.Uint16,
        value = 3200
    )

    print('setExposureIndexResponse: ' + str(setExposureIndexResponse))

    exposureIndex = await client.getDevicePropValue(
        prop = DevicePropertyType.ExposureIndex.value,
        propType = PropertyType.Uint16
    )

    print('Exposure index : ' + str(exposureIndex))

PtpIpClient(usePtpIpClient)

```

OR use CLI

```
python3 console.py --help
python3 console.py device  --discover=True --report=d5300.html
python3 console.py propdesc --name=ExposureIndex
python3 console.py getprop --debug=False --name=ExposureIndex
python3 console.py setprop --debug=False --name=ExposureIndex --value=6400
python3 console.py capture --debug=False > cap.jpg
python3 console.py capture --debug=False --output=cap.jpg
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
