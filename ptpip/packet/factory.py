import struct

from .init_cmd_req import PtpIpInitCmdReq
from .init_cmd_ack import PtpIpInitCmdAck
from .event_req import PtpIpEventReq
from .event_ack import PtpIpEventAck
from .init_fail import PtpIpInitFail
from .cmd_request import PtpIpCmdRequest
from .cmd_response import PtpIpCmdResponse
from .start_data import PtpIpStartDataPacket
from .data import PtpIpDataPacket
from .end_data import PtpIpEndDataPacket
from .ping import PtpIpPing

class PtpIpPacketFactory(object):

    def createPacket(data = None):
        if data is None:
            return None

        cmdtype = struct.unpack('I', data[0:4])[0]

        if cmdtype == 1:
            print("InitCmdReq")
            return PtpIpInitCmdReq(data[4:])
        elif cmdtype == 2:
            print("InitCmdAck")
            return PtpIpInitCmdAck(data[4:])
        elif cmdtype == 3:
            print("EventReq")
            return PtpIpEventReq(data[4:])
        elif cmdtype == 4:
            print("EventAck")
            return PtpIpEventAck(data[4:])
        elif cmdtype == 5:
            print("InitFail")
            return PtpIpInitFail(data[4:])
        elif cmdtype == 6:
            print("CmdRequest")
            return PtpIpCmdRequest(data[4:])
        elif cmdtype == 7:
            print("CmdResponse")
            return PtpIpCmdResponse(data[4:])
        elif cmdtype == 9:
            print("StartDataPacket")
            return PtpIpStartDataPacket(data[4:])
        elif cmdtype == 10:
            print("DataPacket")
            return PtpIpDataPacket(data[4:])
        elif cmdtype == 12:
            print("EndDataPacket")
            return PtpIpEndDataPacket(data[4:])
        elif cmdtype == 13:
            print("Ping")
            return PtpIpPing(data[4:])
        elif cmdtype == 14:
            print("GetDeviceInfo")
        else:
            print("Unknown")

        return None
