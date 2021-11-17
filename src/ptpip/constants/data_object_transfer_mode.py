from enum import Enum

class DataObjectTransferMode(Enum):
    NoTransfer = 0x00
    Receive = 0x01
    Send = 0x02
    SendAndReceive = 0x03
