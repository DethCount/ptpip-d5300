from ptpip.constants.device.shutter_speed import ShutterSpeed
from ptpip.constants.object.focusing_judgement import FocusingJudgement
from ptpip.constants.object.live_view_display_rotation import LiveViewDisplayRotation

from ptpip.data_object.auto_focus_frame import AutoFocusFrame

from ptpip.constants.on_off_property import OnOffProperty

from ptpip.packet.stream_reader import StreamReader

class LiveViewObject():
    def __init__(self, packet, data):
        super(LiveViewObject, self).__init__()

        self.packet = packet

        self.thumbWidth = None
        self.thumbHeight = None
        self.imageWidth = None
        self.imageHeight = None
        self.displayWidth = None
        self.displayHeight = None
        self.displayCenterX = None
        self.displayCenterY = None
        self.autoFocusWidth = None
        self.autoFocusHeight = None
        self.autoFocusCenterX = None
        self.autoFocusCenterY = None
        self.reserve = None
        self.selectedFocusArea = None
        self.rotationDirection = None
        self.focusDrivingStatus = None
        self.reserve2 = None
        self.shutterSpeedId = None
        self.shutterSpeed = None
        self.fNumber = None
        self.countDownTime = None
        self.focusingJudgement = None
        self.autoFocusDrivingEnabled = None
        self.reserve3 = None
        self.levelAngle = None
        self.autoFocusModeStatusOfFaceDetection = None
        self.reserve4 = None
        self.numberOfDetectedFaces = None
        self.autoFocusFramesLength = None
        self.autoFocusFrames = []
        self.reserve5 = None
        self.content = None

        if data is not None:
            reader = StreamReader(data)

            self.unknown = reader.readBytes(7)
            self.thumbWidth = reader.readUint16()
            self.thumbHeight = reader.readUint16()
            self.imageWidth = reader.readUint16()
            self.imageHeight = reader.readUint16()
            self.displayWidth = reader.readUint16()
            self.displayHeight = reader.readUint16()
            self.displayCenterX = reader.readUint16()
            self.displayCenterY = reader.readUint16()
            self.autoFocus = AutoFocusFrame(reader.readBytes(8))

            self.reserve = reader.readBytes(4) # 4
            self.selectedFocusArea = reader.readUint8()

            self.rotationDirection = LiveViewDisplayRotation(reader.readUint8())
            self.focusDrivingStatus = OnOffProperty(reader.readUint8())
            self.reserve2 = reader.readBytes(1) # 1
            self.shutterSpeedId = reader.readUint32()
            self.shutterSpeed = ShutterSpeed(self.shutterSpeedId) \
                if self.shutterSpeedId in ShutterSpeed._value2member_map_ \
                else None

            self.fNumber = reader.readUint16()
            self.countDownTime = reader.readUint16()

            self.focusingJudgementId = reader.readUint8()
            self.focusingJudgement = FocusingJudgement(self.focusingJudgementId) \
                if self.focusingJudgementId in FocusingJudgement._value2member_map_ \
                else None
            self.autoFocusDrivingEnabled = OnOffProperty(reader.readUint8())
            self.reserve3 = reader.readUint16()
            self.levelAngle = reader.readUint32()
            self.autoFocusModeStatusOfFaceDetection = OnOffProperty(reader.readUint8())
            self.reserve4 = reader.readUint8()
            self.numberOfDetectedFaces = reader.readUint8()

            # self.unknown2 = reader.readBytes(0)
            self.autoFocusFramesLength = reader.readUint8()
            for idx in range(0, self.autoFocusFramesLength):
                frame = AutoFocusFrame(reader.readBytes(8))
                self.autoFocusFrames.append(frame)

            self.reserve5 = reader.readBytes(36)
            self.unknown3 = reader.readToPos(256 + 128)
            self.content = reader.readRest()

    def __str__(self):
        sAFFrames = ''
        for frame in self.autoFocusFrames:
            sAFFrames += str(frame)

        return self.__class__.__name__ + ': ' + "\n" \
            + "\t" + 'thumbWidth: ' + str(self.thumbWidth) + "\n" \
            + "\t" + 'thumbHeight: ' + str(self.thumbHeight) + "\n" \
            + "\t" + 'imageWidth: ' + str(self.imageWidth) + "\n" \
            + "\t" + 'imageHeight: ' + str(self.imageHeight) + "\n" \
            + "\t" + 'displayWidth: ' + str(self.displayWidth) + "\n" \
            + "\t" + 'displayHeight: ' + str(self.displayHeight) + "\n" \
            + "\t" + 'displayCenterX: ' + str(self.displayCenterX) + "\n" \
            + "\t" + 'displayCenterY: ' + str(self.displayCenterY) + "\n" \
            + "\t" + 'autoFocus: ' + str(self.autoFocus) + "\n" \
            + "\t" + 'reserve: ' + str(self.reserve) + "\n" \
            + "\t" + 'selectedFocusArea: ' + str(self.selectedFocusArea) + "\n" \
            + "\t" + 'rotationDirection: ' + str(self.rotationDirection) + "\n" \
            + "\t" + 'focusDrivingStatus: ' + str(self.focusDrivingStatus) + "\n" \
            + "\t" + 'reserve2: ' + str(self.reserve2) + "\n" \
            + "\t" + 'shutterSpeedId: ' + str(self.shutterSpeedId) + "\n" \
            + "\t" + 'shutterSpeed: ' + str(
                self.shutterSpeed.name \
                    if self.shutterSpeed is not None
                    else ''
            ) + "\n" \
            + "\t" + 'fNumber: ' + str(self.fNumber) + "\n" \
            + "\t" + 'countDownTime: ' + str(self.countDownTime) + "\n" \
            + "\t" + 'focusingJudgement: ' + (
                self.focusingJudgement.name \
                    if self.focusingJudgement is not None
                    else ''
            ) + "\n" \
            + "\t" + 'autoFocusDrivingEnabled: ' + self.autoFocusDrivingEnabled.name + "\n" \
            + "\t" + 'reserve3: ' + str(self.reserve3) + "\n" \
            + "\t" + 'levelAngle: ' + str(self.levelAngle) + "\n" \
            + "\t" + 'autoFocusModeStatusOfFaceDetection: ' + self.autoFocusModeStatusOfFaceDetection.name + "\n" \
            + "\t" + 'reserve4: ' + str(self.reserve4) + "\n" \
            + "\t" + 'numberOfDetectedFaces: ' + str(self.numberOfDetectedFaces) + "\n" \
            + "\t" + 'autoFocusFramesLength: ' + str(self.autoFocusFramesLength) + "\n" \
            + "\t" + 'autoFocusFrames: ' + sAFFrames + "\n" \
            + "\t" + 'reserve5: ' + str(self.reserve5) + "\n"
            # + "\t" + 'content: ' + str(self.content) + "\n"
