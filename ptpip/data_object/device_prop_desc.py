from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.on_off_property import OnOffProperty

from ptpip.constants.device.auto_off_time import AutoOffTime
from ptpip.constants.device.auto_meter_off_delay import AutoMeterOffDelay
from ptpip.constants.device.beep import Beep
from ptpip.constants.device.exposure_ev_step import ExposureEVStep
from ptpip.constants.device.exposure_index import ExposureIndex
from ptpip.constants.device.exposure_metering_mode import ExposureMeteringMode
from ptpip.constants.device.exposure_program_mode import ExposureProgramMode
from ptpip.constants.device.exposure_time import ExposureTime
from ptpip.constants.device.flash_mode import FlashMode
from ptpip.constants.device.focus_metering_mode import FocusMeteringMode
from ptpip.constants.device.focus_mode import FocusMode
from ptpip.constants.device.lcd_power_off import LCDPowerOff
from ptpip.constants.device.read_mode import ReadMode
from ptpip.constants.device.remote_control_delay import RemoteControlDelay
from ptpip.constants.device.scene_mode import SceneMode
from ptpip.constants.device.self_timer_delay import SelfTimerDelay
from ptpip.constants.device.self_timer_shoot_expose import SelfTimerShootExpose
from ptpip.constants.device.still_capture_mode import StillCaptureMode
from ptpip.constants.device.wb_tune_fluorescent import WbTuneFluorescent
from ptpip.constants.device.white_balance import WhiteBalance

from ptpip.constants.property_type import PropertyType
from ptpip.constants.property_type_mutation import PropertyTypeMutation

from ptpip.data_object import DataObject

class DevicePropDesc():
    def __init__(self, packet, data):
        super(DevicePropDesc, self).__init__()

        self.packet = packet
        if data == None:
            return

        pos = 0
        (self.type_id, pos) = DataObject.ParseUint16(data, pos)
        self.type = DevicePropertyType(self.type_id) \
            if self.type_id in DevicePropertyType._value2member_map_ \
            else None

        (self.prop_type_id, pos) = DataObject.ParseUint16(data, pos)
        self.prop_type = PropertyType(self.prop_type_id) \
            if self.prop_type_id in PropertyType._value2member_map_ \
            else None

        (self.mode, pos) = DataObject.ParseUint8(data, pos)
        self.mode = ReadMode(self.mode)

        if self.prop_type == None:
            return

        (self.default_value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
        (self.value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)

        self.mutation = None

        (self.mutation, pos) = DataObject.ParseUint8(data, pos)
        self.mutation = PropertyTypeMutation(self.mutation)

        self.min_value = None
        self.max_value = None
        self.step = None
        self.values = None

        try:
            if self.mutation == PropertyTypeMutation.Range:
                (self.min_value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
                (self.max_value, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
                (self.step, pos) = DataObject.ParseType(self.prop_type.name, data, pos)
            elif self.mutation == PropertyTypeMutation.Enumeration:
                (self.values, pos) = DataObject.ParseArray(self.prop_type.name, data, pos, 'Uint16')
        except Exception as e:
            print(str(e))

    def propertyValueStr(self, value):
        if self.type == DevicePropertyType.AutoMeterOffDelay \
            and value in AutoMeterOffDelay._value2member_map_ \
            :
                return AutoMeterOffDelay(value).name

        if self.type == DevicePropertyType.AutoOffTime \
            and value in AutoOffTime._value2member_map_ \
            :
                return AutoOffTime(value).name

        if self.type == DevicePropertyType.Beep \
            and value in Beep._value2member_map_ \
            :
                return Beep(value).name

        if self.type == DevicePropertyType.ExposureEVStep \
            and value in ExposureEVStep._value2member_map_ \
            :
                return ExposureEVStep(value).name

        if self.type == DevicePropertyType.ExposureIndex \
            and value in ExposureIndex._value2member_map_ \
            :
                return ExposureIndex(value).name

        if self.type == DevicePropertyType.ExposureMeteringMode \
            and value in ExposureMeteringMode._value2member_map_ \
            :
                return ExposureMeteringMode(value).name

        if self.type == DevicePropertyType.ExposureProgramMode \
            and value in ExposureProgramMode._value2member_map_ \
            :
                return ExposureProgramMode(value).name

        if self.type == DevicePropertyType.ExposureTime \
            and value in ExposureTime._value2member_map_ \
            :
                return ExposureTime(value).name

        if self.type == DevicePropertyType.FlashMode \
            and value in FlashMode._value2member_map_ \
            :
                return FlashMode(value).name

        if self.type == DevicePropertyType.FocusMeteringMode \
            and value in FocusMeteringMode._value2member_map_ \
            :
                return FocusMeteringMode(value).name

        if self.type == DevicePropertyType.FocusMode \
            and value in FocusMode._value2member_map_ \
            :
                return FocusMode(value).name

        if self.type == DevicePropertyType.ISOAutoHighLimit \
            and value in ExposureIndex._value2member_map_ \
            :
                return ExposureIndex(value).name

        if self.type == DevicePropertyType.ISOAutoShutterTime \
            and value in ExposureTime._value2member_map_ \
            :
                return ExposureTime(value).name

        if self.type == DevicePropertyType.LCDPowerOff \
            and value in LCDPowerOff._value2member_map_ \
            :
                return LCDPowerOff(value).name

        if self.type == DevicePropertyType.RemoteControlDelay \
            and value in RemoteControlDelay._value2member_map_ \
            :
                return RemoteControlDelay(value).name

        if self.type == DevicePropertyType.SelfTimerDelay \
            and value in SelfTimerDelay._value2member_map_ \
            :
                return SelfTimerDelay(value).name

        if self.type == DevicePropertyType.SelfTimerShootExpose \
            and value in SelfTimerShootExpose._value2member_map_ \
            :
                return SelfTimerShootExpose(value).name

        if self.type == DevicePropertyType.SceneMode \
            and value in SceneMode._value2member_map_ \
            :
                return SceneMode(value).name

        if self.type == DevicePropertyType.StillCaptureMode \
            and value in StillCaptureMode._value2member_map_ \
            :
                return StillCaptureMode(value).name

        if self.type == DevicePropertyType.WbTuneFluorescent \
            and value in WbTuneFluorescent._value2member_map_ \
            :
                return WbTuneFluorescent(value).name

        if self.type == DevicePropertyType.WhiteBalance \
            and value in WhiteBalance._value2member_map_ \
            :
                return WhiteBalance(value).name

        if self.type in (
            DevicePropertyType.ISOAutoControl,
            DevicePropertyType.AELockRelease
        ) and value in OnOffProperty._value2member_map_ \
        :
            return OnOffProperty(value).name

        return str(value)

    def __str__(self):
        sMutation = ''
        if self.mutation == PropertyTypeMutation.Range:
            if self.min_value != 0 and self.max_value != 0:
                sMutation += "\t" + 'min_value: ' + self.propertyValueStr(self.min_value) + "\n" \
                    + "\t" + 'max_value: ' + self.propertyValueStr(self.min_value) + "\n"

            if self.step != 1:
                sMutation += "\t" + 'step: ' + str(self.step) + "\n"
        elif self.mutation == PropertyTypeMutation.Enumeration:
            sValues = []
            for value in self.values:
                sValues.append(self.propertyValueStr(value))

            sMutation = "\t" + 'values: ' + str(sValues) + "\n"

        return 'DevicePropDesc: ' + "\n" \
            + "\t" + 'type_id: ' + str(self.type_id) + "\n" \
            + "\t" + 'type: ' + str(self.type) + "\n" \
            + "\t" + 'prop_type_id: ' + str(self.prop_type_id) + "\n" \
            + "\t" + 'prop_type: ' + str(self.prop_type) + "\n" \
            + "\t" + 'mode: ' + str(self.mode.name) + "\n" \
            + "\t" + 'default_value: ' + self.propertyValueStr(self.default_value) + "\n" \
            + "\t" + 'value: ' + self.propertyValueStr(self.value) + "\n" \
            + "\t" + 'mutation: ' + str(self.mutation) + "\n" \
            + sMutation
