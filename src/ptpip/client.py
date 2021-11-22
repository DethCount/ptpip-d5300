import asyncio
import struct

from threading import Thread

from ptpip.connection import Connection

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.event_type import EventType
from ptpip.constants.property_type import PropertyType
from ptpip.constants.response_code import ResponseCode
from ptpip.constants.data_object_transfer_mode import DataObjectTransferMode

from ptpip.constants.device.property_type import DevicePropertyType

from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.stream_writer import StreamWriter
from ptpip.packet.cmd_request import CmdRequest
from ptpip.packet.cmd_response import CmdResponse

from ptpip.data_object.data_object import DataObject
from ptpip.data_object.device_info import DeviceInfo
from ptpip.data_object.device_prop_desc import DevicePropDesc
from ptpip.data_object.object_handle_array import ObjectHandleArray
from ptpip.data_object.object_info import ObjectInfo
from ptpip.data_object.storage_id_array import StorageIdArray
from ptpip.data_object.storage_info import StorageInfo

class PtpIpClient():
    def __init__(
        self,
        middleware,
        host = None,
        port = None,
        communicationThreadDelay = 0,
        debug = False
    ):
        super(PtpIpClient, self).__init__()

        self.host = host
        self.port = port
        self.communicationThreadDelay = communicationThreadDelay
        self.debug = debug == True

        self.conn = Connection(debug = debug)
        self.conn.open(
            host = self.host,
            port = self.port
        )

        # Start the Thread which is constantly checking the status of the camera
        # and which is processing new command packages which should be send
        threadComm = Thread(
            target = self.conn.communicationThread,
            args = (communicationThreadDelay,)
        )

        threadComm.daemon = True
        threadComm.start()

        eventLoop = asyncio.get_event_loop()

        try:
            eventLoop.run_until_complete(
                middleware(self)
            )
        except KeyboardInterrupt:
            eventLoop.stop()
            pass

    async def getDeviceInfo(self, delay = 0, transactionId = None):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetDeviceInfo.value
        )
        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId :
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, DeviceInfo):
                    return objData
                elif isinstance(objData, DataObject) \
                    and isinstance(objData.packet, CmdResponse) \
                :
                    return objData.packet.code
                else:
                    return None

    async def discoverDevicePropDesc(
        self,
        device: DeviceInfo,
        delay = 0,
        more = False
    ):
        discovered = []
        for propId in range(1, 65536):
            if propId in device.properties \
                or (
                    not more
                    and propId not in DevicePropertyType._value2member_map_
                ) \
            :
                continue

            response = await self.getDevicePropDesc(
                propId,
                delay = delay,
                transactionId = self.conn.createTransaction()
            )

            if isinstance(response, ResponseCode):
                continue

            discovered.append(response)

        return discovered


    async def getDevicePropDesc(self, prop, delay = 0, transactionId = None):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetDevicePropDesc.value,
            param1 = prop
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, DevicePropDesc):
                    return objData
                elif isinstance(objData, DataObject) \
                    and isinstance(objData.packet, CmdResponse) \
                :
                    return objData.packet.code
                else:
                    return None

    async def setDevicePropValue(
        self,
        prop,
        propType: PropertyType,
        value,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.SetDevicePropValue.value,
            param1 = prop,
            dataObjectTransferMode = DataObjectTransferMode.Send,
            dataObject = DataObject(
                data = StreamWriter() \
                    .writeType(propType.name, value) \
                    .data
            )
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, DataObject):
                    if isinstance(objData.packet, CmdResponse) \
                        and objData.packet.code \
                            != ResponseCode.OK.value \
                    :
                        return objData.packet.code
                    return objData
                else:
                    return None

    async def getDevicePropValue(
        self,
        prop,
        propType: PropertyType,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetDevicePropValue.value,
            param1 = prop
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, DataObject):
                    if isinstance(objData.packet, CmdResponse) \
                        and objData.packet.code \
                            != ResponseCode.OK.value \
                    :
                        return objData.packet.code
                    return StreamReader(objData.data) \
                        .readType(propType.name)
                else:
                    return None

    async def initCapture(
        self,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.InitiateCapture.value,
            param1 = 0,
            param2 = 0
        )

        self.conn.sendCmd(cmd)

        foundEvent = False
        async for event in self.conn.listenEventQueue(delay = delay):
            if event.type == EventType.ObjectAdded:
                self.conn.eventQueue.remove(event)
                foundEvent = event
                break

        if not foundEvent:
            raise(Exception('Couldn\'t receive capture event'))

        objTransactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = objTransactionId,
            cmd = CmdType.GetObject.value,
            param1 = event.parameter
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if isinstance(objData, DataObject) \
                and objData.packet.transactionId == objTransactionId \
            :
                self.conn.objectQueue.remove(objData)
                return objData.data

    async def getStorageIds(
        self,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetStorageIDs.value
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, StorageIdArray):
                    return objData
                elif isinstance(objData, CmdResponse):
                    return objData.code
                else:
                    return None

    async def getStorageInfo(
        self,
        storageId,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetStorageInfo.value,
            param1 = storageId
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, StorageInfo):
                    return objData
                elif isinstance(objData, CmdResponse):
                    return objData.code
                else:
                    return None

    async def getNumObjects(
        self,
        storageId,
        objectFormatId = None,
        handle = None,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetNumObjects.value,
            param1 = storageId,
            param2 = objectFormatId,
            param3 = handle
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData.packet, CmdResponse):
                    if objData.packet.code != ResponseCode.OK:
                        return objData.packet.code
                    elif len(objData.packet.parameters) > 0:
                        return objData.packet.parameters[0];
                    else:
                        return None
                else:
                    return None

    async def getObjectHandles(
        self,
        storageId = None,
        objectFormatId = None,
        handle = None,
        allStorages = True,
        allFormats = True,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetObjectHandles.value,
            param1 = storageId \
                if storageId is not None \
                    or not allStorages \
                else 0xFFFFFFFF,
            param2 = objectFormatId \
                if objectFormatId is not None \
                    or not allFormats \
                else 0xFFFFFFFF,
            param3 = handle
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, ObjectHandleArray):
                    return objData
                elif isinstance(objData, CmdResponse):
                    return objData.code
                else:
                    return None

    async def getObjectInfo(
        self,
        handle,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            transactionId = self.conn.createTransaction()

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetObjectInfo.value,
            param1 = handle
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, ObjectInfo):
                    return objData
                elif isinstance(objData, CmdResponse):
                    return objData.code
                else:
                    return None

    async def getPictureControlCapabilities(
        self,
        picCtrlItem,
        defaultFlag = 0x00,
        delay = 0,
        transactionId = None
    ):
        if transactionId == None:
            self.lastTransactionId += 1
            transactionId = self.lastTransactionId

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.GetPicCtrlCapability.value,
            param1 = picCtrlItem,
            param2 = defaultFlag
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if isinstance(objData, DataObject) \
                and objData.packet.transactionId == transactionId \
            :
                self.objectQueue.remove(objData)

                return objData
