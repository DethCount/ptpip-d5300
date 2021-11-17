from ptpip.constants.device.property_type import DevicePropertyType
from ptpip.constants.device.on_off_property import OnOffProperty

from ptpip.constants.device.active_pic_ctrl_item import ActivePicCtrlItem
from ptpip.constants.device.ae_bracketing_step import AEBracketingStep
from ptpip.constants.device.ae_af_lock_setting import AEAFLockSetting
from ptpip.constants.device.af_mode_select import AFModeSelect
from ptpip.constants.device.auto_off_time import AutoOffTime
from ptpip.constants.device.auto_meter_off_delay import AutoMeterOffDelay
from ptpip.constants.device.bracketing_type import BracketingType
from ptpip.constants.device.beep import Beep
from ptpip.constants.device.command_dial_rotation import CommandDialRotation
from ptpip.constants.device.date_count_display_setting import DateCountDisplaySetting
from ptpip.constants.device.date_counter_select import DateCounterSelect
from ptpip.constants.device.date_imprint_setting import DateImprintSetting
from ptpip.constants.device.exposure_ev_step import ExposureEVStep
from ptpip.constants.device.exposure_display_status import ExposureDisplayStatus
from ptpip.constants.device.exposure_index import ExposureIndex
from ptpip.constants.device.exposure_indicate_status import ExposureIndicateStatus
from ptpip.constants.device.exposure_metering_mode import ExposureMeteringMode
from ptpip.constants.device.exposure_program_mode import ExposureProgramMode
from ptpip.constants.device.exposure_time import ExposureTime
from ptpip.constants.device.external_speed_light_sort import ExternalSpeedLightSort
from ptpip.constants.device.external_speed_light_status import ExternalSpeedLightStatus
from ptpip.constants.device.flash_compensation import FlashCompensation
from ptpip.constants.device.flash_mode import FlashMode
from ptpip.constants.device.flexible_program import FlexibleProgram
from ptpip.constants.device.focus_area import FocusArea
from ptpip.constants.device.focus_metering_mode import FocusMeteringMode
from ptpip.constants.device.focus_mode import FocusMode
from ptpip.constants.device.function_button import FunctionButton
from ptpip.constants.device.indicator_display import IndicatorDisplay
from ptpip.constants.device.internal_flash_compensation import InternalFlashCompensation
from ptpip.constants.device.internal_flash_manual import InternalFlashManual
from ptpip.constants.device.internal_flash_mode import InternalFlashMode
from ptpip.constants.device.internal_flash_status import InternalFlashStatus
from ptpip.constants.device.lcd_power_off import LCDPowerOff
from ptpip.constants.device.lens_sort import LensSort
from ptpip.constants.device.live_view_screen_display_setting import LiveViewScreenDisplaySetting
from ptpip.constants.device.new_external_speed_light_mode import NewExternalSpeedLightMode
from ptpip.constants.device.numbering_mode import NumberingMode
from ptpip.constants.device.orientation import Orientation
from ptpip.constants.device.read_mode import ReadMode
from ptpip.constants.device.recording_media import RecordingMedia
from ptpip.constants.device.remote_control_delay import RemoteControlDelay
from ptpip.constants.device.scene_mode import SceneMode
from ptpip.constants.device.self_timer_delay import SelfTimerDelay
from ptpip.constants.device.self_timer_shoot_expose import SelfTimerShootExpose
from ptpip.constants.device.shutter_speed import ShutterSpeed
from ptpip.constants.device.still_capture_mode import StillCaptureMode
from ptpip.constants.device.warning_status import WarningStatus
from ptpip.constants.device.wb_bracketing_step import WBBracketingStep
from ptpip.constants.device.wb_tune_fluorescent import WBTuneFluorescent
from ptpip.constants.device.white_balance import WhiteBalance

from ptpip.constants.property_type import PropertyType
from ptpip.constants.property_type_mutation import PropertyTypeMutation

from ptpip.packet.stream_reader import StreamReader
from ptpip.data_object.data_object import DataObject

class DevicePropDesc():
    def __init__(self, packet, data):
        super(DevicePropDesc, self).__init__()

        self.packet = packet
        if data == None:
            return

        reader = StreamReader(data = data)

        self.typeId = reader.readUint16()
        self.type = DevicePropertyType(self.typeId) \
            if self.typeId in DevicePropertyType._value2member_map_ \
            else None

        self.propTypeId = reader.readUint16()
        self.propType = PropertyType(self.propTypeId) \
            if self.propTypeId in PropertyType._value2member_map_ \
            else None

        self.mode = ReadMode(reader.readUint8())

        if self.propType == None:
            return

        self.defaultValue = reader.readType(self.propType.name)
        self.value = reader.readType(self.propType.name)

        self.mutation = PropertyTypeMutation(reader.readUint8())

        self.minValue = None
        self.maxValue = None
        self.step = None
        self.values = None

        try:
            if self.mutation == PropertyTypeMutation.Range:
                self.minValue = reader.readType(self.propType.name)
                self.maxValue = reader.readType(self.propType.name)
                self.step = reader.readType(self.propType.name)
            elif self.mutation == PropertyTypeMutation.Enumeration:
                self.values = reader.readArray(
                    self.propType.name,
                    lengthTypeName = PropertyType.Uint16.name
                )
        except Exception as e:
            print(str(e))

    def propertyValueStr(self, value):
        if self.type == DevicePropertyType.ActivePicCtrlItem \
            and value in ActivePicCtrlItem._value2member_map_ \
            :
                return ActivePicCtrlItem(value).name

        if self.type == DevicePropertyType.AEBracketingStep \
            and value in AEBracketingStep._value2member_map_ \
            :
                return AEBracketingStep(value).name

        if self.type == DevicePropertyType.AEAFLockSetting \
            and value in AEAFLockSetting._value2member_map_ \
            :
                return AEAFLockSetting(value).name

        if self.type == DevicePropertyType.AFModeSelect \
            and value in AFModeSelect._value2member_map_ \
            :
                return AFModeSelect(value).name

        if self.type == DevicePropertyType.AutoMeterOffDelay \
            and value in AutoMeterOffDelay._value2member_map_ \
            :
                return AutoMeterOffDelay(value).name

        if self.type == DevicePropertyType.AutoOffTime \
            and value in AutoOffTime._value2member_map_ \
            :
                return AutoOffTime(value).name

        if self.type == DevicePropertyType.BracketingType \
            and value in BracketingType._value2member_map_ \
            :
                return BracketingType(value).name

        if self.type == DevicePropertyType.Beep \
            and value in Beep._value2member_map_ \
            :
                return Beep(value).name

        if self.type == DevicePropertyType.CommandDialRotation \
            and value in CommandDialRotation._value2member_map_ \
            :
                return CommandDialRotation(value).name

        if self.type == DevicePropertyType.DateCountDisplaySetting \
            and value in DateCountDisplaySetting._value2member_map_ \
            :
                return DateCountDisplaySetting(value).name

        if self.type == DevicePropertyType.DateCounterSelect \
            and value in DateCounterSelect._value2member_map_ \
            :
                return DateCounterSelect(value).name

        if self.type == DevicePropertyType.DateImprintSetting \
            and value in DateImprintSetting._value2member_map_ \
            :
                return DateImprintSetting(value).name

        if self.type == DevicePropertyType.ExposureEVStep \
            and value in ExposureEVStep._value2member_map_ \
            :
                return ExposureEVStep(value).name

        if self.type == DevicePropertyType.ExposureDisplayStatus \
            and value in ExposureDisplayStatus._value2member_map_ \
            :
                return ExposureDisplayStatus(value).name

        if self.type == DevicePropertyType.ExposureIndex \
            and value in ExposureIndex._value2member_map_ \
            :
                return ExposureIndex(value).name

        if self.type == DevicePropertyType.ExposureIndicateStatus \
            and value in ExposureIndicateStatus._value2member_map_ \
            :
                return ExposureIndicateStatus(value).name

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

        if self.type == DevicePropertyType.ExternalSpeedLightSort \
            and value in ExternalSpeedLightSort._value2member_map_ \
            :
                return ExternalSpeedLightSort(value).name

        if self.type == DevicePropertyType.ExternalSpeedLightStatus \
            and value in ExternalSpeedLightStatus._value2member_map_ \
            :
                return ExternalSpeedLightStatus(value).name

        if self.type == DevicePropertyType.FlashMode \
            and value in FlashMode._value2member_map_ \
            :
                return FlashMode(value).name

        if self.type == DevicePropertyType.FlashCompensation \
            and value in FlashCompensation._value2member_map_ \
            :
                return FlashCompensation(value).name

        if self.type == DevicePropertyType.FlexibleProgram \
            and value in FlexibleProgram._value2member_map_ \
            :
                return FlexibleProgram(value).name

        if self.type == DevicePropertyType.FocusArea \
            and value in FocusArea._value2member_map_ \
            :
                return FocusArea(value).name

        if self.type == DevicePropertyType.FocusMeteringMode \
            and value in FocusMeteringMode._value2member_map_ \
            :
                return FocusMeteringMode(value).name

        if self.type == DevicePropertyType.FocusMode \
            and value in FocusMode._value2member_map_ \
            :
                return FocusMode(value).name

        if self.type == DevicePropertyType.FunctionButton \
            and value in FunctionButton._value2member_map_ \
            :
                return FunctionButton(value).name

        if self.type == DevicePropertyType.IndicatorDisplay \
            and value in IndicatorDisplay._value2member_map_ \
            :
                return IndicatorDisplay(value).name

        if self.type == DevicePropertyType.InternalFlashCompensation \
            and value in InternalFlashCompensation._value2member_map_ \
            :
                return InternalFlashCompensation(value).name

        if self.type == DevicePropertyType.InternalFlashManual \
            and value in InternalFlashManual._value2member_map_ \
            :
                return InternalFlashManual(value).name

        if self.type == DevicePropertyType.InternalFlashMode \
            and value in InternalFlashMode._value2member_map_ \
            :
                return InternalFlashMode(value).name

        if self.type == DevicePropertyType.InternalFlashStatus \
            and value in InternalFlashStatus._value2member_map_ \
            :
                return InternalFlashStatus(value).name

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

        if self.type == DevicePropertyType.LensSort \
            and value in LensSort._value2member_map_ \
            :
                return LensSort(value).name

        if self.type == DevicePropertyType.LiveViewScreenDisplaySetting \
            and value in LiveViewScreenDisplaySetting._value2member_map_ \
            :
                return LiveViewScreenDisplaySetting(value).name

        if self.type == DevicePropertyType.NewExternalSpeedLightMode \
            and value in NewExternalSpeedLightMode._value2member_map_ \
            :
                return NewExternalSpeedLightMode(value).name

        if self.type == DevicePropertyType.NumberingMode \
            and value in NumberingMode._value2member_map_ \
            :
                return NumberingMode(value).name

        if self.type == DevicePropertyType.Orientation \
            and value in Orientation._value2member_map_ \
            :
                return Orientation(value).name

        if self.type == DevicePropertyType.RecordingMedia \
            and value in RecordingMedia._value2member_map_ \
            :
                return RecordingMedia(value).name

        if self.type == DevicePropertyType.RemoteControlDelay \
            and value in RemoteControlDelay._value2member_map_ \
            :
                return RemoteControlDelay(value).name

        if self.type == DevicePropertyType.SceneMode \
            and value in SceneMode._value2member_map_ \
            :
                return SceneMode(value).name

        if self.type == DevicePropertyType.SelfTimerDelay \
            and value in SelfTimerDelay._value2member_map_ \
            :
                return SelfTimerDelay(value).name

        if self.type == DevicePropertyType.SelfTimerShootExpose \
            and value in SelfTimerShootExpose._value2member_map_ \
            :
                return SelfTimerShootExpose(value).name

        if self.type == DevicePropertyType.ShutterSpeed \
            and value in ShutterSpeed._value2member_map_ \
            :
                return ShutterSpeed(value).name

        if self.type == DevicePropertyType.ShutterSpeed2 \
            and value in ShutterSpeed._value2member_map_ \
            :
                return ShutterSpeed(value).name

        if self.type == DevicePropertyType.StillCaptureMode \
            and value in StillCaptureMode._value2member_map_ \
            :
                return StillCaptureMode(value).name

        if self.type == DevicePropertyType.WarningStatus \
            and value in WarningStatus._value2member_map_ \
            :
                return WarningStatus(value).name

        if self.type == DevicePropertyType.WBBracketingStep \
            and value in WBBracketingStep._value2member_map_ \
            :
                return WBBracketingStep(value).name

        if self.type == DevicePropertyType.WBTuneFluorescent \
            and value in WBTuneFluorescent._value2member_map_ \
            :
                return WBTuneFluorescent(value).name

        if self.type == DevicePropertyType.WhiteBalance \
            and value in WhiteBalance._value2member_map_ \
            :
                return WhiteBalance(value).name

        if self.type in (
            DevicePropertyType.AELockRelease,
            DevicePropertyType.AELockStatus,
            DevicePropertyType.AFLockStatus,
            DevicePropertyType.EnableBracketing,
            DevicePropertyType.EnableComment,
            DevicePropertyType.EnableShutter,
            DevicePropertyType.ExposureDelay,
            DevicePropertyType.ExposureIndicateLightup,
            DevicePropertyType.ExternalDCIn,
            DevicePropertyType.ExternalSpeedLightExist,
            DevicePropertyType.FinderISODisplay,
            DevicePropertyType.GridDisplay,
            DevicePropertyType.InfoDisplayErrorStatus,
            DevicePropertyType.InternalFlashPopup,
            DevicePropertyType.ISOAutoControl,
            DevicePropertyType.OrientationSensorMode
        ) and value in OnOffProperty._value2member_map_ \
        :
            return OnOffProperty(value).name

        return str(value)

    def __str__(self):
        sMutation = ''
        if self.mutation == PropertyTypeMutation.Range:
            if self.minValue != 0 and self.maxValue != 0:
                sMutation += "\t" \
                    + 'min_value: ' \
                        + self.propertyValueStr(self.minValue) + "\n" \
                    + "\t" \
                    + 'max_value: ' \
                        + self.propertyValueStr(self.maxValue) + "\n"

            if self.step != 1:
                sMutation += "\t" + 'step: ' + str(self.step) + "\n"
        elif self.mutation == PropertyTypeMutation.Enumeration:
            sValues = []
            for value in self.values:
                sValues.append(self.propertyValueStr(value))

            sMutation = "\t" + 'values: ' + str(sValues) + "\n"

        return 'DevicePropDesc: ' + "\n" \
            + "\t" + 'typeId: ' + str(self.typeId) + "\n" \
            + "\t" + 'type: ' + str(self.type) + "\n" \
            + "\t" + 'propTypeId: ' + str(self.propTypeId) + "\n" \
            + "\t" + 'propType: ' + str(self.propType) + "\n" \
            + "\t" + 'mode: ' + str(self.mode.name) + "\n" \
            + "\t" + 'defaultValue: ' \
                + self.propertyValueStr(self.defaultValue) + "\n" \
            + "\t" + 'value: ' \
                + self.propertyValueStr(self.value) + "\n" \
            + "\t" + 'mutation: ' + str(self.mutation) + "\n" \
            + sMutation
