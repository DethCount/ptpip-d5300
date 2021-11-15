import asyncio
import struct

from threading import Thread

from ptpip.connection import Connection

from ptpip.constants.cmd_type import CmdType
from ptpip.constants.property_type import PropertyType
from ptpip.constants.response_code import ResponseCode

from ptpip.constants.device.property_type import DevicePropertyType

from ptpip.packet.stream_reader import StreamReader
from ptpip.packet.cmd_request import CmdRequest
from ptpip.packet.cmd_response import CmdResponse

from ptpip.data_object.data_object import DataObject
from ptpip.data_object.device_info import DeviceInfo
from ptpip.data_object.device_prop_desc import DevicePropDesc

class PtpIpClient():
    def __init__(
        self,
        middleware,
        host = None,
        port = None,
        communicationThreadDelay = 0
    ):
        super(PtpIpClient, self).__init__()

        self.host = host
        self.port = port
        self.communicationThreadDelay = communicationThreadDelay
        self.lastTransactionId = 2021;

        self.conn = Connection()
        self.conn.open(self.host, self.port)

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
        print('getDeviceInfo')
        if transactionId == None:
            self.lastTransactionId += 1
            transactionId = self.lastTransactionId

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
                elif isinstance(objData, DataObject):
                    return ResponseCode(objData.packet.responseCode)
                else:
                    return None

    async def discoverDevicePropDesc(
        self,
        device: DeviceInfo,
        delay = 0
    ):
        print('discoverDevicePropDesc')
        discovered = []
        for idx, prop in enumerate(DevicePropertyType._value2member_map_):
            if prop == DevicePropertyType.Undefined.value \
                or prop in device.properties \
            :
                continue

            self.lastTransactionId += 1

            response = await self.getDevicePropDesc(
                prop,
                delay = delay,
                transactionId = self.lastTransactionId
            )

            if isinstance(response, ResponseCode):
                print(DevicePropertyType(prop).name + ': ' + response.name)
                continue

            discovered.append(response)

        return discovered


    async def getDevicePropDesc(self, prop, delay = 0, transactionId = None):
        print('getDevicePropDesc')
        if transactionId == None:
            self.lastTransactionId += 1
            transactionId = self.lastTransactionId

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
                elif isinstance(objData, DataObject):
                    return ResponseCode(objData.packet.responseCode)
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
        print('setDevicePropValue')
        if transactionId == None:
            self.lastTransactionId += 1
            transactionId = self.lastTransactionId

        cmd = CmdRequest(
            transactionId = transactionId,
            cmd = CmdType.SetDevicePropValue.value,
            param1 = prop,
            paramType1 = PropertyType.Uint32,
            param2 = value,
            paramType2 = propType
        )

        self.conn.sendCmd(cmd)

        async for objData in self.conn.listenObjectDataQueue(delay = delay):
            if objData.packet.transactionId == transactionId:
                self.conn.objectQueue.remove(objData)
                if isinstance(objData, DataObject):
                    if isinstance(objData.packet, CmdResponse) \
                        and objData.packet.responseCode \
                            != ResponseCode.OK.value \
                    :
                        return ResponseCode(objData.packet.responseCode)
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
        print('getDevicePropValue')
        if transactionId == None:
            self.lastTransactionId += 1
            transactionId = self.lastTransactionId

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
                        and objData.packet.responseCode \
                            != ResponseCode.OK.value \
                    :
                        return ResponseCode(objData.packet.responseCode)
                    return StreamReader(objData.data) \
                        .readType(propType.name)
                else:
                    return None

    async def getPictureControlCapabilities(
        self,
        picCtrlItem,
        defaultFlag = 0x00,
        delay = 0,
        transactionId = None
    ):
        print('getPictureControlCapabilities')
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
