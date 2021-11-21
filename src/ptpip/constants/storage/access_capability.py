from enum import Enum

class AccessCapability(Enum):
    ReadWrite                       = 0
    ReadOnlyWithoutObjectDeletion   = 1
    ReadOnlyWithObjectDeletion      = 2
