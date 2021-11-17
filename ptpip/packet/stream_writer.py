import struct

from ptpip.constants.property_type import PropertyType

class StreamWriter():
    def __init__(self, data = None):
        super(StreamWriter, self).__init__()

        self.data = b'' if data == None else data

    def writeBytes(self, value):
        self.data += value
        return self

    def writeInt8(self, value):
        self.data += struct.pack('b', value)
        return self

    def writeUint8(self, value):
        self.data += struct.pack('B', value)
        return self

    def writeInt16(self, value):
        self.data += struct.pack('h', value)
        return self

    def writeUint16(self, value):
        self.data += struct.pack('H', value)
        return self

    def writeInt32(self, value):
        self.data += struct.pack('i', value)
        return self

    def writeUint32(self, value):
        self.data += struct.pack('I', value)
        return self

    def writeInt64(self, value):
        self.data += struct.pack('q', value)
        return self

    def writeUint64(self, value):
        self.data += struct.pack('Q', value)
        return self

    def writeString(self, value):
        length = len(value)
        self.writeUint8(length)

        for i in range(0, length):
            self.writeUint16(value[i])

        return self

    def writeArrayByLength(self, typeLength, values):
        length = len(values)
        self.writeUint32(length)

        for i in range(0, length):
            for j in range(0, typeLength):
                self.writeUint8(values[i * typeLength + j])

        return self

    def writeArray(
        self,
        typeName,
        values,
        lengthTypeName = PropertyType.Uint32.name
    ):
        length = len(values)
        self.writeType(lengthTypeName, length)

        for i in range(0, length):
            self.writeType(typeName, values[i])

        return self

    def writeInt8Array(self, values):
        return self.writeArray(PropertyType.Int8.name, values)
    def writeUint8Array(self, values):
        return self.writeArray(PropertyType.Uint8.name, values)

    def writeInt16Array(self, values):
        return self.writeArray(PropertyType.Int16.name, values)
    def writeUint16Array(self, values):
        return self.writeArray(PropertyType.Uint16.name, values)

    def writeInt32Array(self, values):
        return self.writeArray(PropertyType.Int32.name, values)
    def writeUint32Array(self, values):
        return self.writeArray(PropertyType.Uint32.name, values)

    def writeInt64Array(self, values):
        return self.writeArray(PropertyType.Int64.name, values)
    def writeUint64Array(self, values):
        return self.writeArray(PropertyType.Uint64.name, values)

    def writeType(self, typeName, value):
        if typeName == PropertyType.Int8.name:
            return self.writeInt8(value)
        if typeName == PropertyType.Uint8.name:
            return self.writeUint8(value)

        if typeName == PropertyType.Int16.name:
            return self.writeInt16(value)
        if typeName == PropertyType.Uint16.name:
            return self.writeUint16(value)

        if typeName == PropertyType.Int32.name:
            return self.writeInt32(value)
        if typeName == PropertyType.Uint32.name:
            return self.writeUint32(value)

        if typeName == PropertyType.Int64.name:
            return self.writeInt64(value)
        if typeName == PropertyType.Uint64.name:
            return self.writeUint64(value)

        if typeName == PropertyType.String.name:
            return self.writeString(value)

        if typeName == PropertyType.Int8Array.name:
            return self.writeInt8Array(value)
        if typeName == PropertyType.Uint8Array.name:
            return self.writeUint8Array(value)

        if typeName == PropertyType.Int16Array.name:
            return self.writeInt16Array(value)
        if typeName == PropertyType.Uint16Array.name:
            return self.writeUint16Array(value)

        if typeName == PropertyType.Int32Array.name:
            return self.writeInt32Array(value)
        if typeName == PropertyType.Uint32Array.name:
            return self.writeUint32Array(value)

        if typeName == PropertyType.Int64Array.name:
            return self.writeInt64Array(value)
        if typeName == PropertyType.Uint64Array.name:
            return self.writeUint64Array(value)

        print('Unknown type: ' + str(typeName))
        return self
