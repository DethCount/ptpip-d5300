import socket
import struct
import time

from ptpip.cmd_type import CmdType
from ptpip.data_object.data_object import PtpIpDataObject
from ptpip.event.factory import PtpIpEventFactory
from ptpip.packet.factory import PtpIpPacketFactory
from ptpip.packet.cmd_request import PtpIpCmdRequest
from ptpip.packet.cmd_response import PtpIpCmdResponse
from ptpip.packet.start_data import PtpIpStartDataPacket
from ptpip.packet.data import PtpIpDataPacket
from ptpip.packet.init_cmd_ack import PtpIpInitCmdAck
from ptpip.packet.init_cmd_req import PtpIpInitCmdReq
from ptpip.packet.event_req import PtpIpEventReq

class PtpIpConnection(object):

    """docstring for PtpIP"""
    def __init__(self):
        super(PtpIpConnection, self).__init__()
        self.session = None
        self.session_events = None
        self.session_id = None
        self.cmd_queue = []
        self.event_queue = []
        self.object_queue = []

    def open(self, host='192.168.1.1', port=15740):
        # Open both session, first one for for commands, second for events
        self.session = self.connect(host=host, port=port)
        self.send_receive_ptpip_packet(PtpIpInitCmdReq(), self.session)
        self.session_events = self.connect(host=host, port=port)
        self.send_receive_ptpip_packet(PtpIpEventReq(), self.session_events)

        print("session_id: " + str(struct.unpack('I', self.session_id)[0]))
        ptpip_cmd = PtpIpCmdRequest(
            transaction_id=0,
            cmd=CmdType.OpenSession.value,
            param1=struct.unpack('I', self.session_id)[0]
        )
        self.send_receive_ptpip_packet(ptpip_cmd, self.session)


    def communication_thread(self):
        while True:
            if len(self.cmd_queue) == 0:
                # do a ping receive a pong (same as ping) as reply to keep the connection alive
                # couldnt get any reply onto a propper PtpIpPing packet so i am querying the status
                # of the device
                print("Ping...")
                ptpip_packet_reply = self.send_receive_ptpip_packet(
                    PtpIpCmdRequest(
                        transaction_id=6,
                        cmd=CmdType.DeviceReady.value
                    ),
                    self.session
                )

                if isinstance(ptpip_packet_reply, PtpIpCmdResponse):
                    time.sleep(1)
                    continue
            else:
                # get the next command from command the queue
                ptpip_cmd = self.cmd_queue.pop()
                print("Pop : " + str(struct.unpack('I', ptpip_cmd.cmdtype)[0]))
                ptpip_packet_reply = self.send_receive_ptpip_packet(ptpip_cmd, self.session)
                if (ptpip_packet_reply.ptp_response_code == 0x2001 \
                        and ptpip_packet_reply.ptp_response_code == 0x2019):
                    print("Cmd send successfully")
                else:
                    print("cmd reply is: " + str(ptpip_packet_reply.ptp_response_code))

            # wait 1 second before new packets are processed/send to the camera
            time.sleep(1)
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

    def send_receive_ptpip_packet(self, ptpip_packet, session):
        if isinstance(ptpip_packet, PtpIpInitCmdReq):
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

            # set the session id of the object if the reply is of type PtpIpInitCmdAck
            if isinstance(ptpip_packet_reply, PtpIpInitCmdAck):
                self.session_id = ptpip_packet_reply.session_id

        elif isinstance(ptpip_packet, PtpIpEventReq):
            self.send_ptpip_event_req(ptpip_packet, session)

            ptpip_packet_reply = self.get_response_packet(session)

        elif isinstance(ptpip_packet, PtpIpCmdRequest) \
            and ptpip_packet.ptp_cmd == CmdType.GetEvent.value:
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

            # download object data
            if isinstance(ptpip_packet_reply, PtpIpStartDataPacket):
                data_length = struct.unpack('I', ptpip_packet_reply.length)[0]

                ptpip_packet_reply = self.get_response_packet(session)
                data = ptpip_packet_reply.data
                while isinstance(ptpip_packet_reply, PtpIpDataPacket):
                    data = data + ptpip_packet_reply.data
                    ptpip_packet_reply = self.get_response_packet(session)

            if data_length == len(data):
                events = PtpIpEventFactory(data).get_events()
                for event in events:
                    self.event_queue.append(event)

            ptpip_packet_reply = self.get_response_packet(session)

        elif isinstance(ptpip_packet, PtpIpCmdRequest) \
            and (
                ptpip_packet.ptp_cmd == CmdType.GetObject.value
                or ptpip_packet.ptp_cmd == CmdType.GetDeviceInfo.value
            ):
            self.send_packet(ptpip_packet, session)
            ptpip_packet_reply = self.get_response_packet(session)

            if isinstance(ptpip_packet_reply, PtpIpStartDataPacket):
                data_length = struct.unpack('I', ptpip_packet_reply.length)[0]

                ptpip_packet_reply = self.get_response_packet(session)
                data = ptpip_packet_reply.data
                while isinstance(ptpip_packet_reply, PtpIpDataPacket):
                    data = data + ptpip_packet_reply.data
                    ptpip_packet_reply = self.get_response_packet(session)

            if data_length == len(data):
                self.object_queue.append(PtpIpDataObject(ptpip_packet, data))

            ptpip_packet_reply = self.get_response_packet(session)

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
        response = PtpIpPacketFactory.createPacket(data=self.receive_data(session))
        print('---- RECV ----')
        print('CmdType: ' + str(struct.unpack('I', response.cmdtype)[0]))
        return response
