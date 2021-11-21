from ptpip.data_object.uint32_array import Uint32Array

class StorageIdArray(Uint32Array):
    def __init__(self, packet, data):
        super(StorageIdArray, self).__init__(packet, data)

        self.sdCardInserted = None

        if data is not None:
            self.sdCardInserted = len(self.elements) > 0 \
                and self.elements[0] == 0x00010001

    def __str__(self):
        return super.__str__(self) \
            + "\t" + 'sdCardInserted: ' + str(self.sdCardInserted) + "\n"
