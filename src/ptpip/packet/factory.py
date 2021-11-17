import struct

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

        cmdtype = reader.readUint32()

        if cmdtype == 1:
            # print("InitCmdReq")
            return InitCmdReq(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        elif cmdtype == 2:
            # print("InitCmdAck")
            return InitCmdAck(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                sessionId = sessionId
            )
        elif cmdtype == 3:
            # print("EventReq")
            return EventReq(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                sessionId = sessionId
            )
        elif cmdtype == 4:
            # print("EventAck")
            return EventAck(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                sessionId = sessionId,
                request = request
            )
        elif cmdtype == 5:
            # print("InitFail")
            return InitFail(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        elif cmdtype == 6:
            # print("CmdRequest")
            return CmdRequest(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        elif cmdtype == 7:
            # print("CmdResponse")
            return CmdResponse(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif cmdtype == 9:
            # print("StartDataPacket")
            return StartDataPacket(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif cmdtype == 10:
            # print("DataPacket")
            return DataPacket(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif cmdtype == 12:
            # print("EndDataPacket")
            return EndDataPacket(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode,
                request = request
            )
        elif cmdtype == 13:
            # print("Ping")
            return Ping(
                data = reader.readRest(),
                transactionId = transactionId,
                dataObject = dataObject,
                dataObjectTransferMode = dataObjectTransferMode
            )
        # elif cmdtype == 14:
            # print("GetDeviceInfo")
        else:
            print("Unknown cmdtype: " + str(cmdtype))

        return None
