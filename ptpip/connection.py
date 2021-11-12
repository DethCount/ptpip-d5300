import asyncio
import socket
import struct
import time

from ptpip.cmd_type import CmdType
from ptpip.data_object.data_object import DataObject
from ptpip.data_object.device_prop_desc import DevicePropDesc
from ptpip.event.factory import EventFactory
from ptpip.packet.factory import PacketFactory
from ptpip.packet.cmd_request import CmdRequest
from ptpip.packet.cmd_response import CmdResponse
from ptpip.packet.start_data import StartDataPacket
from ptpip.packet.data import DataPacket
from ptpip.packet.init_cmd_ack import InitCmdAck
from ptpip.packet.init_cmd_req import InitCmdReq
from ptpip.packet.event_req import EventReq

from ptpip.data_object.device_info import DeviceInfo

class Connection(object):

    """docstring for PtpIP"""
    def __init__(self):
        super(Connection, self).__init__()
        self.session = None
        self.session_events = None
        self.session_id = None
        self.cmd_queue = []
        self.event_queue = []
        self.object_queue = []

    def open(self,
        host='192.168.1.1',
        port=15740,
        transaction_id=0,
        communication_thread_delay=1
    ):
        # Open both session, first one for for commands, second for events
        self.session = self.connect(host=host, port=port)
        self.send_receive_ptpip_packet(InitCmdReq(), self.session)
        self.session_events = self.connect(host=host, port=port)
        self.send_receive_ptpip_packet(EventReq(), self.session_events)

        print("session_id: " + str(struct.unpack('I', self.session_id)[0]))
        ptpip_cmd = CmdRequest(
            transaction_id=transaction_id,
            cmd=CmdType.OpenSession.value,
            param1=struct.unpack('I', self.session_id)[0]
        )
        self.send_receive_ptpip_packet(ptpip_cmd, self.session)

    def communication_thread(self, delay = 1):
        print('Communication: ' + str(type(delay)) + ' ' + str(delay))
        while True:
            print('Comm while')
            if len(self.cmd_queue) == 0:
                # do a ping receive a pong (same as ping) as reply to keep the connection alive
                # couldnt get any reply onto a propper Ping packet so i am querying the status
                # of the device
                print("CCC Ping...")
                ptpip_packet_reply = self.send_receive_ptpip_packet(
                    CmdRequest(
                        transaction_id=6,
                        cmd=CmdType.DeviceReady.value
                    ),
                    self.session
                )
                print('Ping end')
            else:
                # get the next command from command the queue
                ptpip_cmd = self.cmd_queue.pop()
                print("CCC Pop : " + str(struct.unpack('I', ptpip_cmd.cmdtype)[0]))
                ptpip_packet_reply = self.send_receive_ptpip_packet(ptpip_cmd, self.session)
                if (ptpip_packet_reply.ptp_response_code == 0x2001 \
                        and ptpip_packet_reply.ptp_response_code == 0x2019):
                    print("CCC Cmd send successfully")
                else:
                    print("CCC Cmd reply is: " + str(ptpip_packet_reply.ptp_response_code))

            # wait delay seconds before new packets are processed/send to the camera
            print('Comm delay start')
            time.sleep(delay)
            print('Comm delay end')

        print('End comm')

    def queue_object(self, data_object):
        cmdtype = data_object.packet.ptp_cmd
        transaction_id = struct.unpack('I', data_object.packet.transaction_id)[0]

        sCmdType = CmdType(cmdtype).name \
            if cmdtype in CmdType._value2member_map_ \
            else str(cmdtype)

        print('OOO Response to ' + sCmdType + ', transaction_id: ' + str(transaction_id))

        if cmdtype == CmdType.GetDeviceInfo.value:
            device = DeviceInfo(data_object.packet, data_object.data)
            print(str(device))
            self.object_queue.append(device)
        elif cmdtype == CmdType.GetObject.value:
            data_stream = io.BytesIO(data_object.data)
            img = Image.open(data_stream)
            print('OOO Image')
            self.object_queue.append(img)
            # img.save('/tmp/test_' + str(idx) + '.jpg')
        elif cmdtype == CmdType.GetDevicePropDesc.value:
            device_prop_desc = DevicePropDesc(data_object.packet, data_object.data)
            print(str(device_prop_desc))
            self.object_queue.append(device_prop_desc)
        else:
            print('OOO Ignored: ' + sCmdType)
            self.object_queue.append(data_object)

    async def listen_object_data_queue(self, delay = 1):
        while True:
            print('OOO Objects in queue: ' + str(len(self.object_queue)))

            for idx, data_object in enumerate(self.object_queue):
                yield data_object

            time.sleep(delay)
            pass

    def send_ptpip_cmd(self, ptpip_packet):
        self.cmd_queue.append(ptpip_packet)

    def connect(self, host='192.168.1.1', port=15740):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            s.connect((host, port))
        except socket.error as err:
            if s:
                s.close()
            print("Could not open socket: " + str(err))
        return s

    async def get_device_info(self, delay=1, transaction_id=1):
        print('get_device_info')
        ptpip_cmd = CmdRequest(
            transaction_id=transaction_id,
            cmd=CmdType.GetDeviceInfo.value
        )
        self.send_ptpip_cmd(ptpip_cmd)

        async for obj_data in self.listen_object_data_queue(delay = delay):
            if isinstance(obj_data, DeviceInfo) \
                and struct.unpack('I', obj_data.packet.transaction_id)[0] == transaction_id \
            :
                self.object_queue.remove(obj_data)
                return obj_data

    async def get_device_prop_desc(self, prop, delay=1, transaction_id=1):
        print('get_device_prop_desc')
        ptpip_cmd = CmdRequest(
            transaction_id=transaction_id,
            cmd=CmdType.GetDevicePropDesc.value,
            param1=prop
        )
        self.send_ptpip_cmd(ptpip_cmd)

        async for obj_data in self.listen_object_data_queue(delay = delay):
            if isinstance(obj_data, DevicePropDesc) \
                and struct.unpack('I', obj_data.packet.transaction_id)[0] == transaction_id \
            :
                self.object_queue.remove(obj_data)
                return obj_data

    async def get_picture_control_capabilities(self, delay=1, transaction_id=1):
        print('get_picture_control_capabilities')
        ptpip_cmd = CmdRequest(
            transaction_id=transaction_id,
            # cmd=CmdType.GetPicCtrlCapability.value
            cmd=CmdType.GetPicCtrlData.value
        )
        self.send_ptpip_cmd(ptpip_cmd)

        async for obj_data in self.listen_object_data_queue(delay = delay):
            if isinstance(obj_data, DataObject) \
                and struct.unpack('I', obj_data.packet.transaction_id)[0] == transaction_id \
            :
                self.object_queue.remove(obj_data)
                return obj_data

    def send_receive_ptpip_packet(self, ptpip_packet, session):
        if isinstance(ptpip_packet, InitCmdReq):
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

            # set the session id of the object if the reply is of type InitCmdAck
            if isinstance(ptpip_packet_reply, InitCmdAck):
                self.session_id = ptpip_packet_reply.session_id

        elif isinstance(ptpip_packet, EventReq):
            self.send_ptpip_event_req(ptpip_packet, session)

            ptpip_packet_reply = self.get_response_packet(session)

        elif isinstance(ptpip_packet, CmdRequest) \
            and ptpip_packet.ptp_cmd == CmdType.GetEvent.value \
        :
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

            # download object data
            if isinstance(ptpip_packet_reply, StartDataPacket):
                data_length = struct.unpack('I', ptpip_packet_reply.length)[0]

                ptpip_packet_reply = self.get_response_packet(session)
                data = ptpip_packet_reply.data
                while isinstance(ptpip_packet_reply, DataPacket):
                    data = data + ptpip_packet_reply.data
                    ptpip_packet_reply = self.get_response_packet(session)

                if data_length == len(data):
                    events = EventFactory(data).get_events()
                    for event in events:
                        self.event_queue.append(event)

            ptpip_packet_reply = self.get_response_packet(session)

        elif isinstance(ptpip_packet, CmdRequest) \
            and (
                ptpip_packet.ptp_cmd == CmdType.GetObject.value
                or ptpip_packet.ptp_cmd == CmdType.GetDeviceInfo.value
                or ptpip_packet.ptp_cmd == CmdType.GetDevicePropDesc.value
                or ptpip_packet.ptp_cmd == CmdType.GetPicCtrlCapability.value
                or ptpip_packet.ptp_cmd == CmdType.GetPicCtrlData.value
            ):
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

            data_length = 0
            if isinstance(ptpip_packet_reply, StartDataPacket):
                data_length = struct.unpack('I', ptpip_packet_reply.length)[0]

                ptpip_packet_reply = self.get_response_packet(session)
                data = ptpip_packet_reply.data
                while isinstance(ptpip_packet_reply, DataPacket):
                    data = data + ptpip_packet_reply.data
                    ptpip_packet_reply = self.get_response_packet(session)

                if data_length == len(data):
                    self.queue_object(DataObject(ptpip_packet, data))

                ptpip_packet_reply = self.get_response_packet(session)
            else:
                print(str(type(ptpip_packet_reply)))
                print(str(ptpip_packet_reply))

        else:
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

        return ptpip_packet_reply

    def send_ptpip_event_req(self, ptpip_packet, session):
        # add the session id of the object itself if it is not specified in the package
        if ptpip_packet.session_id is None:
            ptpip_packet.session_id = self.session_id

        self.send_packet(ptpip_packet, session)

    def send_data(self, data, session):
        session.send(struct.pack('I', len(data) + 4) + data)

    def send_packet(self, packet, session):
        print('---- SEND ----')
        print('CmdType: ' + str(struct.unpack('I', packet.cmdtype)[0]))
        self.send_data(packet.data(), session)

    def receive_data(self, session):
        data = session.recv(4)
        (data_length,) = struct.unpack('I', data)
        # print("RECV Data length: " + str(data_length))
        while data_length > len(data):
            data += session.recv(data_length - len(data))
        return data[4:]

    def get_response_packet(self, session):
        response = PacketFactory.createPacket(data=self.receive_data(session))
        print('---- RECV ----')
        print('CmdType: ' + str(struct.unpack('I', response.cmdtype)[0]))
        return response
