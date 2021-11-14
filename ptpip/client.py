import asyncio
import struct

from threading import Thread

from ptpip.connection import Connection

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.response_code import ResponseCode
from ptpip.constants.device.property_type import DevicePropertyType

from ptpip.packet.cmd_request import CmdRequest

from ptpip.data_object.data_object import DataObject
from ptpip.data_object.device_info import DeviceInfo
from ptpip.data_object.device_prop_desc import DevicePropDesc

class PtpIpClient():
    def __init__(
        self,
        middleware,
        host = None,
        port = None,
        communicationThreadDelay = 0
    ):
        super(PtpIpClient, self).__init__()

        self.host = host
        self.port = port
        self.communicationThreadDelay = communicationThreadDelay

        self.conn = Connection()
        self.conn.open(self.host, self.port)

        # Start the Thread which is constantly checking the status of the camera
        # and which is processing new command packages which should be send
        thread_comm = Thread(
            target = self.conn.communication_thread,
            args = (communicationThreadDelay,)
        )

        thread_comm.daemon = True
        thread_comm.start()

        event_loop = asyncio.get_event_loop()

        try:
            event_loop.run_until_complete(
                middleware(self)
            )
        except KeyboardInterrupt:
            event_loop.stop()
            pass

    async def get_device_info(self, delay = 0, transaction_id = 1):
        print('get_device_info')
        cmd = CmdRequest(
            transaction_id = transaction_id,
            cmd = CmdType.GetDeviceInfo.value
        )
        self.conn.send_cmd(cmd)

        async for obj_data in self.conn.listen_object_data_queue(delay = delay):
            if struct.unpack('I', obj_data.packet.transaction_id)[0] \
                 == transaction_id \
            :
                self.conn.object_queue.remove(obj_data)
                if isinstance(obj_data, DeviceInfo):
                    return obj_data
                elif isinstance(obj_data, DataObject):
                    return ResponseCode(obj_data.packet.ptp_response_code)
                else:
                    return None

    async def discover_device_prop_desc(
        self,
        device: DeviceInfo,
        delay = 0,
        transaction_id = 1
    ):
        print('discover_device_prop_desc')
        discovered = []
        for idx, prop in enumerate(DevicePropertyType._value2member_map_):
            if prop == DevicePropertyType.Undefined.value \
                or prop in device.properties \
            :
                continue

            response = await self.get_device_prop_desc(
                prop,
                delay = delay,
                transaction_id = transaction_id << 3 | idx
            )

            if isinstance(response, ResponseCode):
                print(DevicePropertyType(prop).name + ': ' + response.name)
                continue

            discovered.append(response)

        return discovered


    async def get_device_prop_desc(self, prop, delay = 0, transaction_id = 1):
        print('get_device_prop_desc')
        cmd = CmdRequest(
            transaction_id = transaction_id,
            cmd = CmdType.GetDevicePropDesc.value,
            param1 = prop
        )

        self.conn.send_cmd(cmd)

        async for obj_data in self.conn.listen_object_data_queue(delay = delay):
            obj_transaction_id = struct.unpack(
                'I',
                obj_data.packet.transaction_id
            )[0]

            if obj_transaction_id == transaction_id:
                self.conn.object_queue.remove(obj_data)
                if isinstance(obj_data, DevicePropDesc):
                    return obj_data
                elif isinstance(obj_data, DataObject):
                    return ResponseCode(obj_data.packet.ptp_response_code)
                else:
                    return None

    async def get_picture_control_capabilities(
        self,
        picCtrlItem,
        defaultFlag = 0x00,
        delay = 0,
        transaction_id = 1
    ):
        print('get_picture_control_capabilities')
        cmd = CmdRequest(
            transaction_id = transaction_id,
            cmd = CmdType.GetPicCtrlCapability.value,
            param1 = picCtrlItem,
            param2 = defaultFlag
        )

        self.conn.send_cmd(cmd)

        async for obj_data in self.conn.listen_object_data_queue(delay = delay):
            if isinstance(obj_data, DataObject) \
                and struct.unpack('I', obj_data.packet.transaction_id)[0] \
                    == transaction_id \
            :
                self.object_queue.remove(obj_data)

                return obj_data
