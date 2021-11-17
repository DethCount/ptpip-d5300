from enum import Enum

class LensSort(Enum):
    NotMountedOrNonCPUInternalLensMounted   = 0x00
    CPULensMounted                          = 0x01
