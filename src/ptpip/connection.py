import asyncio
import socket
import struct
import time

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.property_type import PropertyType
from ptpip.constants.response_code import ResponseCode
from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject
from ptpip.data_object.device_info import DeviceInfo
from ptpip.data_object.device_prop_desc import DevicePropDesc

from ptpip.event.factory import EventFactory

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter
from ptpip.packet.factory import PacketFactory
from ptpip.packet.cmd_request import CmdRequest
from ptpip.packet.cmd_response import CmdResponse
from ptpip.packet.start_data import StartDataPacket
from ptpip.packet.data import DataPacket
from ptpip.packet.end_data import EndDataPacket
from ptpip.packet.init_cmd_ack import InitCmdAck
from ptpip.packet.init_cmd_req import InitCmdReq
from ptpip.packet.event_req import EventReq

class Connection():
    DEFAULT_HOST = '192.168.1.1'
    DEFAULT_PORT = 15740

    """docstring for PtpIP"""
    def __init__(self):
        super(Connection, self).__init__()

        self.session = None
        self.sessionEvents = None
        self.sessionId = None
        self.cmdQueue = []
        self.eventQueue = []
        self.objectQueue = []

    def open(self,
        host = None,
        port = None,
        transactionId = 0
    ):
        # Open both session, first one for for commands, second for events
        self.session = self.connect(host = host, port = port)
        self.sendReceivePacket(InitCmdReq(), self.session)

        self.sessionEvents = self.connect(host = host, port = port)
        self.sendReceivePacket(EventReq(), self.sessionEvents)

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.OpenSession.value,
            param1 = self.sessionId,
            paramType1 = PropertyType.Uint32
        )

        self.sendReceivePacket(cmd, self.session)

    def communicationThread(self, delay = 0):
        while True:
            if len(self.cmdQueue) == 0:
                # do a ping receive a pong (same as ping) as reply to keep the connection alive
                # couldnt get any reply onto a propper Ping packet so i am querying the status
                # of the device
                reply = self.sendReceivePacket(
                    CmdRequest(
                        transactionId = 6,
                        cmd = CmdType.DeviceReady.value
                    ),
                    self.session
                )
            else:
                cmd = self.cmdQueue.pop()
                reply = self.sendReceivePacket(cmd, self.session)
                if reply.code != ResponseCode.OK.value \
                    and reply.code != ResponseCode.DeviceBusy.value \
                :
                    print("CCC Cmd reply is: " + str(reply.code))

            time.sleep(delay)
        print(str('End of communication'))

    def queueObject(self, dataObject):
        if not isinstance(dataObject.packet, CmdRequest):
            self.objectQueue.append(dataObject)
            return

        if dataObject.packet.cmd == CmdType.GetDeviceInfo.value:
            device = DeviceInfo(dataObject.packet, dataObject.data)
            self.objectQueue.append(device)
            return

        if dataObject.packet.cmd == CmdType.GetObject.value:
            dataStream = io.BytesIO(dataObject.data)
            img = Image.open(dataStream)
            self.objectQueue.append(img)
            return

        if dataObject.packet.cmd == CmdType.GetEvent.value:
            events = EventFactory(dataObject.data).getEvents()

            for event in events:
                self.eventQueue.append(event)

            return

        if dataObject.packet.cmd == CmdType.GetDevicePropDesc.value \
            and dataObject.data != None \
        :
            devicePropDesc = DevicePropDesc(dataObject.packet, dataObject.data)
            self.objectQueue.append(devicePropDesc)

            return

        self.objectQueue.append(dataObject)

    async def listenObjectDataQueue(self, delay = 0):
        while True:
            # print('OOO Objects in queue: ' + str(len(self.objectQueue)))

            for idx, dataObject in enumerate(self.objectQueue):
                yield dataObject

            time.sleep(delay)
            pass

    def sendCmd(self, packet):
        self.cmdQueue.append(packet)

    def connect(self, host = None, port = None):
        if host == None:
            host = self.DEFAULT_HOST

        if port == None:
            port = self.DEFAULT_PORT

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            s.connect((host, port))
        except socket.error as err:
            if s:
                s.close()
            print("Could not open socket: " + str(err))
        return s

    def sendReceivePacket(self, packet: Packet, session):
        print('sendReceivePacket: ' + str(packet))
        if isinstance(packet, EventReq) and packet.sessionId is None:
            packet.sessionId = self.sessionId

        self.sendPacket(packet, session)
        # print(str(packet.transactionId))

        # send data object
        if packet.dataObject != None \
            and (
                packet.dataObjectTransferMode
                    == DataObjectTransferMode.Send
                or packet.dataObjectTransferMode
                    == DataObjectTransferMode.SendAndReceive
            ) \
        :
            self.sendPacket(
                StartDataPacket(
                    transactionId = packet.transactionId,
                    length = len(packet.dataObject.data)
                ),
                session
            )
            self.sendPacket(
                DataPacket(
                    content = packet.dataObject.data,
                    transactionId = packet.transactionId
                ),
                session
            )
            self.sendPacket(
                EndDataPacket(
                    transactionId = packet.transactionId
                ),
                session
            )

        # receive response
        reply = self.getResponse(session)

        if isinstance(reply, InitCmdAck):
            self.sessionId = reply.sessionId

        # receive data object
        if packet.dataObjectTransferMode \
            != DataObjectTransferMode.NoTransfer \
        :
            dataLength = 0
            if isinstance(reply, StartDataPacket):
                dataLength = reply.length

                reply = self.getResponse(session, request = packet)
                data = reply.data
                while isinstance(reply, DataPacket):
                    data += reply.content
                    reply = self.getResponse(session, request = packet)

                if dataLength == len(data):
                    self.queueObject(DataObject(packet, data = data))

                reply = self.getResponse(session, request = packet)
            else:
                self.queueObject(DataObject(reply, data = None))

        return reply

    def sendEventReq(self, packet: Packet, session):
        # add the session id of the object itself if it is not specified in the package
        if packet.sessionId is None:
            packet.sessionId = self.sessionId

        self.sendPacket(packet, session)

    def sendData(self, data, session):
        session.send(
            StreamWriter() \
                .writeUint32(len(data) + 4) \
                .writeBytes(data) \
                .data
        )

    def sendPacket(self, packet, session):
        print('---- SEND ----')
        print('CmdType: ' + str(packet.cmdtype))
        self.sendData(packet.pack(), session)
        print('---- End SEND ----')

    def receiveData(self, session):
        reader = StreamReader(data = session.recv(4))
        dataLength = reader.readUint32()
        print("RECV Data length: " + str(dataLength))
        while dataLength > len(reader.data):
            reader.data += session.recv(dataLength - len(reader.data))

        return reader.readRest()

    def getResponse(self, session, request: Packet = None):
        response = PacketFactory.createPacket(
            data = self.receiveData(session),
            request = request,
            sessionId = self.sessionId
        )

        print('---- RECV ----')
        print('CmdType: ' + str(response.cmdtype))

        return response
