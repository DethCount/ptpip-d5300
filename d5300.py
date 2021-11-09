import io
import sys
import struct
import time

from ptpip.cmd_type import CmdType
from ptpip.event_type import EventType
from ptpip.connection import PtpIpConnection
from ptpip.packet.cmd_request import PtpIpCmdRequest
from ptpip.data_object.device_info import DeviceInfo

from PIL import Image
from threading import Thread

# START
# open up a PTP/IP connection, default IP and Port is host='192.168.1.1', port=15740
conn = PtpIpConnection()
conn.open()

# Start the Thread which is constantly checking the status of the camera and which is
# processing new command packages which should be send
thread = Thread(target=conn.communication_thread)
thread.daemon = True
thread.start()


# create a PTP/IP command request device info and add it to the queue of the PTP/IP connection object
ptpip_cmd = PtpIpCmdRequest(transaction_id=1, cmd=CmdType.GetDeviceInfo.value)
ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

"""
# create a PTP/IP command request object and add it to the queue of the PTP/IP connection object
ptpip_cmd = PtpIpCmdRequest(
    transaction_id=2,
    cmd=CmdType.InitiateCaptureRecInMedia.value,
    param1=0xffffffff,
    param2=0x0000
)
ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)

# give the thread / connection some time to process the command and thenn close the connection
time.sleep(5)

# get the events from the camera, they will be stored in the event_queue of the ptpip object
ptpip_cmd = PtpIpCmdRequest(
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
        ptpip_cmd = PtpIpCmdRequest(
            transaction_id=4,
            cmd=CmdType.GetObject.value,
            param1=event.event_parameter
        )
        ptpip_packet = conn.send_ptpip_cmd(ptpip_cmd)
"""
# give the thread some time to get the object

while True:
    print('Objects in queue: ' + str(len(conn.object_queue)))

    for idx, data_object in enumerate(conn.object_queue):
        transaction_id = struct.unpack('I', data_object.packet.transaction_id)[0]
        print('Response to transaction ' + str(transaction_id))

        if transaction_id == 1:
            device = DeviceInfo(data_object.data)
            print(str(device))
        elif transaction_id == 4:
            data_stream = io.BytesIO(data_object.data)
            img = Image.open(data_stream)
            img.save('/tmp/test_' + str(idx) + '.jpg')
            print('Image saved')
        else:
            print('Unknown transaction: ' + str(transaction_id))

        conn.object_queue.pop(idx)

    time.sleep(2)

"""
time.sleep(50000000)

sys.exit()
"""
