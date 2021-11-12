import asyncio
import io
import sys
import struct
import time

from ptpip.cmd_type import CmdType
from ptpip.event_type import EventType
from ptpip.device_property_type import DevicePropertyType
from ptpip.exposure_time import ExposureTime
from ptpip.connection import Connection
from ptpip.packet.cmd_request import CmdRequest

from PIL import Image
from threading import Thread, get_ident


def setup():
    conn = Connection()

    conn.open()

    thread_comm = Thread(target=conn.communication_thread, args=(1,))
    thread_comm.daemon = True
    thread_comm.start()

    return conn

async def loop(conn):
    print('loop')
    # START
    # open up a PTP/IP connection, default IP and Port is host='192.168.1.1', port=15740

    # Start the Thread which is constantly checking the status of the camera and which is
    # processing new command packages which should be send


    # thread_obj = Thread(target=conn.treat_object_data_queue, args=(conn, 2))
    # thread_obj.daemon = True
    # thread_obj.start()

    # create a PTP/IP command request device info and add it to the queue of the PTP/IP connection object
    # ptpip_cmd = CmdRequest(transaction_id=1, cmd=CmdType.GetDeviceInfo.value)
    # ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

    device = await conn.get_device_info()
    # print('Device: ' + str(device))

    for idx, prop in enumerate(device.devicePropertiesSupported):
        prop_desc = await conn.get_device_prop_desc(
            prop=prop,
            transaction_id=0x100 | idx
        )
        # print('Prop desc(' + str(idx) + '):' + "\n" + str(prop_desc))

    picture_control_capabilities = await conn.get_picture_control_capabilities(
        transaction_id = 0xFFF
    )

    """
    conn.set_device_prop_desc(
        prop=DevicePropertyType.ExposureIndex.value,
        value="1600",
        transaction_id=0x1000 | idx
    )

    conn.set_device_prop_desc(
        prop=DevicePropertyType.ExposureTime.value,
        value=ExposureTime.OneOver4000.value,
        transaction_id=0x1000 | idx
    )
    """

event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(loop(setup()))

except KeyboardInterrupt:
    event_loop.stop()
    pass

"""
# create a PTP/IP command request object and add it to the queue of the PTP/IP connection object
ptpip_cmd = CmdRequest(
    transaction_id=2,
    cmd=CmdType.InitiateCaptureRecInMedia.value,
    param1=0xffffffff,
    param2=0x0000
)
ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

# give the thread / connection some time to process the command and thenn close the connection
time.sleep(5)

# get the events from the camera, they will be stored in the event_queue of the ptpip object
ptpip_cmd = CmdRequest(
    transaction_id=3,
    cmd=CmdType.GetEvent.value
)
ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

# give the thread some time to process the events it received from the camera
time.sleep(2)

# query the events for the event you are looking for, for example the 0x4002 ObjectAdded if you look
# for a image captured
for event in conn.event_queue:
    if event.event_type == EventType.ObjectAdded.value:
        ptpip_cmd = CmdRequest(
            transaction_id=4,
            cmd=CmdType.GetObject.value,
            param1=event.event_parameter
        )
        ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)
"""
# give the thread some time to get the object

# conn.treat_object_data_queue(conn=conn, delay=2)

"""
time.sleep(50000000)

sys.exit()
"""
