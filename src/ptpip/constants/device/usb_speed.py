from enum import Enum

class USBSpeed(Enum):
    FullSpeed       = 0 # 12 Mbit/s USB 1.0
    HighSpeed       = 1 # 480 Mbit/s USB 1.x and USB 2.0
    SuperSpeed      = 2 # 5.0 Gbit/s USB 3.0 (Unofficial value)
    SuperSpeedPlus  = 3 # 10 Gbit/s USB 3.1 (Unofficial value)
