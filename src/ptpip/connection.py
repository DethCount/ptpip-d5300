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
from ptpip.data_object.object_handle_array import ObjectHandleArray
from ptpip.data_object.object_info import ObjectInfo
from ptpip.data_object.object_prop_code_array import ObjectPropCodeArray
from ptpip.data_object.storage_id_array import StorageIdArray
from ptpip.data_object.storage_info import StorageInfo

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
from ptpip.packet.event_req import EventReq
from ptpip.packet.init_cmd_ack import InitCmdAck
from ptpip.packet.init_cmd_req import InitCmdReq
from ptpip.packet.ping import Ping

class Connection():
    DEFAULT_HOST = '192.168.1.1'
    DEFAULT_PORT = 15740

    """docstring for PtpIP"""
    def __init__(self, debug = False):
        super(Connection, self).__init__()

        self.debug = debug
        self.session = None
        self.sessionEvents = None
        self.sessionId = None
        self.cmdQueue = []
        self.eventQueue = []
        self.objectQueue = []

        self.lastTransactionId = 2021;

    def createTransaction(self):
        self.lastTransactionId += 1

        return self.lastTransactionId

    def open(self,
        host = None,
        port = None,
        transactionId = None
    ):
        # Open both session, first one for for commands, second for events
        self.session = self.connect(host = host, port = port)
        self.sendReceivePacket(InitCmdReq(), self.session)

        self.sessionEvents = self.connect(host = host, port = port)
        self.sendReceivePacket(EventReq(), self.sessionEvents)

        cmd = CmdRequest(
            transactionId = transactionId \
                if transactionId != None \
                else self.createTransaction(),
            cmd = CmdType.OpenSession.value,
            param1 = self.sessionId,
            paramType1 = PropertyType.Uint32
        )

        self.sendReceivePacket(cmd, self.session)

    def communicationThread(self, delay = 0):
        try:
            while True:
                if len(self.cmdQueue) == 0:
                    # do a ping receive a pong (same as ping) as reply to keep the connection alive
                    # couldnt get any reply onto a propper Ping packet so i am querying the status
                    # of the device
                    """
                    reply = self.sendReceivePacket(
                        CmdRequest(
                            transactionId = self.createTransaction(),
                            cmd = CmdType.DeviceReady.value
                        ),
                        self.session
                    )
                    """
                else:
                    cmd = self.cmdQueue.pop()
                    reply = self.sendReceivePacket(cmd, self.session)
                    if self.debug \
                        and reply.code != ResponseCode.OK.value \
                        and reply.code != ResponseCode.DeviceBusy.value \
                    :
                        print("CCC Cmd reply is: " + str(reply.code))

                time.sleep(delay)
        except Exception as err:
            raise(Exception('Error in communication thread: ' + str(err)))

        print(str('End of communication'))

    def queueObject(self, dataObject):
        if not isinstance(dataObject.packet, CmdRequest):
            self.objectQueue.append(dataObject)
            return

        if dataObject.packet.cmd == CmdType.GetEvent:
            events = EventFactory(dataObject.data).getEvents()

            for event in events:
                self.eventQueue.append(event)

            return

        if dataObject.packet.cmd == CmdType.GetDeviceInfo:
            device = DeviceInfo(dataObject.packet, dataObject.data)
            self.objectQueue.append(device)
            return

        if dataObject.packet.cmd == CmdType.GetDevicePropDesc \
            and dataObject.data != None \
        :
            devicePropDesc = DevicePropDesc(dataObject.packet, dataObject.data)
            self.objectQueue.append(devicePropDesc)
            return

        if dataObject.packet.cmd == CmdType.GetStorageIDs:
            storageIds = StorageIdArray(dataObject.packet, dataObject.data)
            self.objectQueue.append(storageIds)
            return

        if dataObject.packet.cmd == CmdType.GetStorageInfo:
            storage = StorageInfo(dataObject.packet, dataObject.data)
            self.objectQueue.append(storage)
            return

        if dataObject.packet.cmd == CmdType.GetObjectHandles:
            handles = ObjectHandleArray(dataObject.packet, dataObject.data)
            self.objectQueue.append(handles)
            return

        if dataObject.packet.cmd == CmdType.GetObjectInfo:
            self.objectQueue.append(ObjectInfo(dataObject.packet, dataObject.data))
            return

        if dataObject.packet.cmd == CmdType.GetObjectPropsSupported:
            self.objectQueue.append(ObjectPropCodeArray(dataObject.packet, dataObject.data))
            return

        self.objectQueue.append(dataObject)

    async def listenObjectDataQueue(self, delay = 0):
        while True:
            # print('OOO Objects in queue: ' + str(len(self.objectQueue)))

            for idx, dataObject in enumerate(self.objectQueue):
                yield dataObject

            time.sleep(delay)
            pass

    async def listenEventQueue(self, delay = 0):
        if delay < 1:
            delay = 1

        while True:
            # print('OOO Events in queue: ' + str(len(self.eventQueue)))

            cmd = CmdRequest(
                cmd = CmdType.GetEvent.value,
                transactionId = self.createTransaction()
            )

            self.sendCmd(cmd)

            for idx, event in enumerate(self.eventQueue):
                yield event

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
            raise(Exception("Could not open socket: " + str(err)))
        return s

    def sendReceivePacket(self, packet: Packet, session):
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
        reply = self.receivePacket(session)

        if isinstance(reply, InitCmdAck):
            self.sessionId = reply.sessionId

        # receive data object
        if packet.dataObjectTransferMode \
            != DataObjectTransferMode.NoTransfer \
        :
            dataLength = 0
            if isinstance(reply, StartDataPacket):
                dataLength = reply.length

                reply = self.receivePacket(session, request = packet)
                data = reply.data
                while isinstance(reply, DataPacket):
                    data += reply.content
                    reply = self.receivePacket(session, request = packet)

                if dataLength == len(data):
                    self.queueObject(DataObject(packet, data = data))

                reply = self.receivePacket(session, request = packet)
            else:
                self.queueObject(DataObject(reply, data = None))

        return reply

    def sendEventReq(self, packet: Packet, session):
        # add the session id of the object itself if it is not specified in the package
        if packet.sessionId is None:
            packet.sessionId = self.sessionId

        self.sendPacket(packet, session)

    def sendPacket(self, packet, session):
        if self.debug:
            print('---- SEND ----')
            print(str(packet))
        self.sendData(packet.pack(), session)

        if self.debug:
            print('---- End SEND ----')

    def receivePacket(self, session, request: Packet = None):
        if self.debug:
            print('---- RECV ----')

        packet = PacketFactory.createPacket(
            data = self.receiveData(session),
            request = request,
            sessionId = self.sessionId
        )

        if self.debug:
            print(str(packet))
            print('---- End RECV ----')

        return packet

    def sendData(self, data, session):
        err = session.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        if 0 != err:
            raise OSError('Socket error: ' + str(err))

        session.send(
            StreamWriter() \
                .writeUint32(len(data) + 4) \
                .writeBytes(data) \
                .data
        )

    def receiveData(self, session, nbTries = 3):
        if self.debug:
            print('RECV DATA')

        err = session.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        if 0 != err:
            raise OSError('Socket error: ' + str(err))

        data = session.recv(4)

        if len(data) < 4:
            if nbTries > 1:
                self.receiveData(session, nbTries - 1)
            else:
                raise(Exception('Communication lost'))

        reader = StreamReader(data = data)
        dataLength = reader.readUint32()

        if self.debug:
            print("RECV Data length: " + str(dataLength))

        while dataLength > len(reader.data):
            reader.data += session.recv(dataLength - len(reader.data))

        return reader.readRest()
