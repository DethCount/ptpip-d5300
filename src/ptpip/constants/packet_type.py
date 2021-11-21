from enum import Enum

class PacketType(Enum):
	InitCmdReq = 1
	InitCmdAck = 2
	EventReq = 3
	EventAck = 4
	InitFail = 5
	CmdRequest = 6
	CmdResponse = 7
	Event = 8
	StartData = 9
	Data = 10
	CancelTransaction = 11
	EndData = 12
	Ping = 13
	Pong = 14
