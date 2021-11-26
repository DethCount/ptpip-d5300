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
# Main Help
python3 console.py --help

# Generate full device report
python3 console.py device  --discover=True --more=True --report=d5300.html

# Get device property description for ExposureIndex
python3 console.py propdesc --name=ExposureIndex

# Get device property value for ExposureIndex
python3 console.py getprop --debug=False --name=ExposureIndex

# Set device property value for ExposureIndex to 6400
python3 console.py setprop --debug=False --name=ExposureIndex --value=6400

# Take a picture with current device configuration and redirect output to cap.jpg
python3 console.py capture --debug=False > cap.jpg

# Take a picture with current device configuration and save it to cap.jpg
python3 console.py capture --debug=False --output=cap.jpg

# List all storage ids
python3 console.py storageids

# Show storage info
python3 console.py storage --id=65537

# Count objects in given storage
python3 console.py numobjects --id=65537

# Lists all Jpeg files on main storage (SDCard) (including example 689504257 handle)
python3 console.py objhandles --id=65537 --formatname=ExifJpeg

# Show object info
python3 console.py objinfo --handle=689504257

# Show object format supported properties
python3 console.py formatprops --name=ExifJpeg --names=True

# Live view writing in cap.jpg at 60 fps
python3 console.py liveimg --output=cap.jpg --fps=60

# Show cap.jpg at 60fps in terminal using Viu : https://github.com/atanunq/viu
while true; do $(viu cap.jpg); sleep 0.016666666666666666; done;

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
