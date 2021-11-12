import struct

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

class PacketFactory(object):

    def createPacket(data = None):
        if data is None:
            return None

        cmdtype = struct.unpack('I', data[0:4])[0]

        if cmdtype == 1:
            print("InitCmdReq")
            return InitCmdReq(data[4:])
        elif cmdtype == 2:
            print("InitCmdAck")
            return InitCmdAck(data[4:])
        elif cmdtype == 3:
            print("EventReq")
            return EventReq(data[4:])
        elif cmdtype == 4:
            print("EventAck")
            return EventAck(data[4:])
        elif cmdtype == 5:
            print("InitFail")
            return InitFail(data[4:])
        elif cmdtype == 6:
            print("CmdRequest")
            return CmdRequest(data[4:])
        elif cmdtype == 7:
            print("CmdResponse")
            return CmdResponse(data[4:])
        elif cmdtype == 9:
            print("StartDataPacket")
            return StartDataPacket(data[4:])
        elif cmdtype == 10:
            print("DataPacket")
            return DataPacket(data[4:])
        elif cmdtype == 12:
            print("EndDataPacket")
            return EndDataPacket(data[4:])
        elif cmdtype == 13:
            print("Ping")
            return Ping(data[4:])
        elif cmdtype == 14:
            print("GetDeviceInfo")
        else:
            print("Unknown")

        return None
