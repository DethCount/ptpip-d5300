import struct

from .packet import Packet
from .stream_reader import StreamReader

from .init_cmd_req import InitCmdReq
from .init_cmd_ack import InitCmdAck
from .event_req import EventReq
from .event_ack import EventAck
from .init_fail import InitFail
from .cmd_request import CmdRequest
from .cmd_response import CmdResponse
from .start_data import StartDataPacket
from .data import DataPacket
from .end_data import EndDataPacket
from .ping import Ping

class PacketFactory():
    def createPacket(data = None, request: Packet = None):
        if data is None:
            return None

        reader = StreamReader(data = data)

        cmdtype = reader.readUint32()

        if cmdtype == 1:
            # print("InitCmdReq")
            return InitCmdReq(reader.readRest())
        elif cmdtype == 2:
            # print("InitCmdAck")
            return InitCmdAck(reader.readRest())
        elif cmdtype == 3:
            # print("EventReq")
            return EventReq(reader.readRest())
        elif cmdtype == 4:
            # print("EventAck")
            return EventAck(reader.readRest(), request = request)
        elif cmdtype == 5:
            # print("InitFail")
            return InitFail(reader.readRest())
        elif cmdtype == 6:
            # print("CmdRequest")
            return CmdRequest(reader.readRest())
        elif cmdtype == 7:
            # print("CmdResponse")
            return CmdResponse(reader.readRest(), request = request)
        elif cmdtype == 9:
            # print("StartDataPacket")
            return StartDataPacket(reader.readRest(), request = request)
        elif cmdtype == 10:
            # print("DataPacket")
            return DataPacket(reader.readRest(), request = request)
        elif cmdtype == 12:
            # print("EndDataPacket")
            return EndDataPacket(reader.readRest(), request = request)
        elif cmdtype == 13:
            # print("Ping")
            return Ping(reader.readRest())
        # elif cmdtype == 14:
            # print("GetDeviceInfo")
        else:
            print("Unknown cmdtype: " + str(cmdtype))

        return None
