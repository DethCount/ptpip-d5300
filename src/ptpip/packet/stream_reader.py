import struct

from ptpip.constants.property_type import PropertyType

class StreamReader():
    def __init__(self, data = None, pos = 0):
        super(StreamReader, self).__init__()

        self.data = data
        self.pos = 0

    def readBytes(self, length = 1):
        pos2 = self.pos + length
        val = self.data[self.pos:pos2]
        self.pos = pos2
        return val

    def readRest(self):
        pos2 = len(self.data)
        val = self.data[self.pos:pos2]
        self.pos = pos2
        return val

    def readInt8(self):
        pos2 = self.pos + 1
        val = struct.unpack('b', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readUint8(self):
        pos2 = self.pos + 1
        val = struct.unpack('B', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readInt16(self):
        pos2 = self.pos + 2
        val = struct.unpack('h', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readUint16(self):
        pos2 = self.pos + 2
        val = struct.unpack('H', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readInt32(self):
        pos2 = self.pos + 4
        val = struct.unpack('i', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readUint32(self):
        pos2 = self.pos + 4
        val = struct.unpack('I', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readInt64(self):
        pos2 = self.pos + 8
        val = struct.unpack('q', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readUint64(self):
        pos2 = self.pos + 8
        val = struct.unpack('Q', self.data[self.pos:pos2])[0]
        self.pos = pos2
        return val

    def readString(self):
        length = self.readUint8()

        s = ''
        for i in range(0, length):
            c = self.readUint16()
            if c == 0:
                break

            s += chr(c)

        return s

    def readArrayByLength(self, typeLength):
        length = self.readUint32()

        results = []
        for i in range(0, length):
            pos2 = self.pos + typeLength
            results.append(self.data[self.pos:pos2])
            self.pos = pos2

        return results

    def readArray(self, typeName, lengthTypeName = PropertyType.Uint32.name):
        length = self.readType(lengthTypeName)

        results = []
        for i in range(0, length):
            results.append(
                self.readType(typeName)
            )

        return results

    def readInt8Array(self):
        return self.readArray(PropertyType.Int8.name)
    def readUint8Array(self):
        return self.readArray(PropertyType.Uint8.name)

    def readInt16Array(self):
        return self.readArray(PropertyType.Int16.name)
    def readUint16Array(self):
        return self.readArray(PropertyType.Uint16.name)

    def readInt32Array(self):
        return self.readArray(PropertyType.Int32.name)
    def readUint32Array(self):
        return self.readArray(PropertyType.Uint32.name)

    def readInt64Array(self):
        return self.readArray(PropertyType.Int64.name)
    def readUint64Array(self):
        return self.readArray(PropertyType.Uint64.name)

    def readType(self, typeName):
        if typeName == PropertyType.Int8.name:
            return self.readInt8()
        if typeName == PropertyType.Uint8.name:
            return self.readUint8()

        if typeName == PropertyType.Int16.name:
            return self.readInt16()
        if typeName == PropertyType.Uint16.name:
            return self.readUint16()

        if typeName == PropertyType.Int32.name:
            return self.readInt32()
        if typeName == PropertyType.Uint32.name:
            return self.readUint32()

        if typeName == PropertyType.Int64.name:
            return self.readInt64()
        if typeName == PropertyType.Uint64.name:
            return self.readUint64()

        if typeName == PropertyType.String.name:
            return self.readString()

        if typeName == PropertyType.Int8Array.name:
            return self.readInt8Array()
        if typeName == PropertyType.Uint8Array.name:
            return self.readUint8Array()

        if typeName == PropertyType.Int16Array.name:
            return self.readInt16Array()
        if typeName == PropertyType.Uint16Array.name:
            return self.readUint16Array()

        if typeName == PropertyType.Int32Array.name:
            return self.readInt32Array()
        if typeName == PropertyType.Uint32Array.name:
            return self.readUint32Array()

        if typeName == PropertyType.Int64Array.name:
            return self.readInt64Array()
        if typeName == PropertyType.Uint64Array.name:
            return self.readUint64Array()
