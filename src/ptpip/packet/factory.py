import struct

from ptpip.constants.packet_type import PacketType
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.data_object.data_object import DataObject

from ptpip.packet.packet import Packet
from ptpip.packet.stream_reader import StreamReader

from ptpip.packet.init_cmd_req import InitCmdReq
from ptpip.packet.init_cmd_ack import InitCmdAck
from ptpip.packet.event_req import EventReq
from ptpip.packet.event_ack import EventAck
from ptpip.packet.init_fail import InitFail
from ptpip.packet.cmd_request import CmdRequest
from ptpip.packet.cmd_response import CmdResponse
from ptpip.packet.start_data import StartDataPacket
from ptpip.packet.data import DataPacket
from ptpip.packet.end_data import EndDataPacket
from ptpip.packet.ping import Ping

class PacketFactory():
    def createPacket(
        data = None,
        transactionId = None,
        dataObject: DataObject = None,
        dataObjectTransferMode: DataObjectTransferMode = None,
        request: Packet = None,
        sessionId = None
    ):
        if data is None:
            return None

        reader = StreamReader(data = data)

        packetType = PacketType(reader.readUint32())
        # print('PacketType: ' + packetType.name);

        if packetType == PacketType.InitCmdReq:
            # print("InitCmdReq")
            return InitCmdReq(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        elif packetType == PacketType.InitCmdAck:
            # print("InitCmdAck")
            return InitCmdAck(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                sessionId = sessionId
            )
        elif packetType == PacketType.EventReq:
            # print("EventReq")
            return EventReq(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                sessionId = sessionId
            )
        elif packetType == PacketType.EventAck:
            # print("EventAck")
            return EventAck(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                sessionId = sessionId,
                request = request
            )
        elif packetType == PacketType.InitFail:
            # print("InitFail")
            return InitFail(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        elif packetType == PacketType.CmdRequest:
            # print("CmdRequest")
            return CmdRequest(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        elif packetType == PacketType.CmdResponse:
            # print("CmdResponse")
            return CmdResponse(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        # elif packetType == PacketType.Event:
            # print("Event")
        elif packetType == PacketType.StartData:
            # print("StartDataPacket")
            return StartDataPacket(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif packetType == PacketType.Data:
            # print("DataPacket")
            return DataPacket(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif packetType == PacketType.EndData:
            # print("EndDataPacket")
            return EndDataPacket(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif packetType == PacketType.Ping:
            # print("Ping")
            return Ping(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        # elif packetType == PacketType.Pong:
            # print("Pong")
        else:
            print("Unknown packet type: " + str(packetType))

        return None
