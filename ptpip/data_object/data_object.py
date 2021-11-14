import struct

class DataObject():
    def __init__(self, packet, data):
        super(DataObject, self).__init__()
        self.packet = packet
        self.data = data

    def __str__(self):
        return 'DataObject: ' + "\n" \
            + "\t" + 'Packet: ' + str(self.packet) + "\n" \
            + "\t" + 'Data: ' + str(self.data) + "\n"

    def ParseInt8(data, pos):
        pos2 = pos + 1
        return (struct.unpack('b', data[pos:pos2])[0], pos2)

    def ParseUint8(data, pos):
        pos2 = pos + 1
        return (struct.unpack('B', data[pos:pos2])[0], pos2)

    def ParseInt16(data, pos):
        pos2 = pos + 2
        return (struct.unpack('h', data[pos:pos2])[0], pos2)

    def ParseUint16(data, pos):
        pos2 = pos + 2
        return (struct.unpack('H', data[pos:pos2])[0], pos2)

    def ParseInt32(data, pos):
        pos2 = pos + 4
        return (struct.unpack('i', data[pos:pos2])[0], pos2)

    def ParseUint32(data, pos):
        pos2 = pos + 4
        return (struct.unpack('I', data[pos:pos2])[0], pos2)

    def ParseInt64(data, pos):
        pos2 = pos + 8
        return (struct.unpack('q', data[pos:pos2])[0], pos2)

    def ParseUint64(data, pos):
        pos2 = pos + 8
        return (struct.unpack('Q', data[pos:pos2])[0], pos2)

    def ParseString(data, pos):
        (length, pos) = DataObject.ParseUint8(data, pos)

        s = ''
        for i in range(0, length):
            (c, pos) = DataObject.ParseUint16(data, pos)
            if c == 0:
                break

            s += chr(c)

        return (s, pos)

    def ParseArrayByLength(typeLength, data, pos):
        (length, pos) = DataObject.ParseUint32(data, pos)

        results = []
        for i in range(0, length):
            pos2 = pos + typeLength
            results.append(data[pos:pos2])
            pos = pos2

        return (results, pos)

    def ParseArray(typeName, data, pos, lengthTypeName = 'Uint32'):
        (length, pos) = DataObject.ParseType(lengthTypeName, data, pos)
        # print(str(length))

        results = []
        for i in range(0, length):
            (item, pos) = DataObject.ParseType(typeName, data, pos)
            # print('item:' + str(item) + '-' + str(type(item)))
            results.append(item)

        return (results, pos)

    def ParseInt8Array(data, pos):
        return self.ParseArray('Int8', data, pos);
    def ParseUint8Array(data, pos):
        return self.ParseArray('Uint8', data, pos);

    def ParseInt16Array(data, pos):
        return self.ParseArray('Int16', data, pos);
    def ParseUint16Array(data, pos):
        return self.ParseArray('Uint16', data, pos);

    def ParseInt32Array(data, pos):
        return self.ParseArray('Int32', data, pos);
    def ParseUint32Array(data, pos):
        return self.ParseArray('Uint32', data, pos);

    def ParseType(typeName, data, pos):
        if typeName == 'Int8':
            return DataObject.ParseInt8(data, pos)
        if typeName == 'Uint8':
            return DataObject.ParseUint8(data, pos)

        if typeName == 'Int16':
            return DataObject.ParseInt16(data, pos)
        if typeName == 'Uint16':
            return DataObject.ParseUint16(data, pos)

        if typeName == 'Int32':
            return DataObject.ParseInt32(data, pos)
        if typeName == 'Uint32':
            return DataObject.ParseUint32(data, pos)

        if typeName == 'Int64':
            return DataObject.ParseInt64(data, pos)
        if typeName == 'Uint64':
            return DataObject.ParseUint64(data, pos)

        if typeName == 'String':
            return DataObject.ParseString(data, pos)

        if typeName == 'Int8Array':
            return DataObject.ParseInt8Array(data, pos)
        if typeName == 'Uint8Array':
            return DataObject.ParseUint8Array(data, pos)

        if typeName == 'Int16Array':
            return DataObject.ParseInt16Array(data, pos)
        if typeName == 'Uint16Array':
            return DataObject.ParseUint16Array(data, pos)

        if typeName == 'Int32Array':
            return DataObject.ParseInt32Array(data, pos)
        if typeName == 'Uint32Array':
            return DataObject.ParseUint32Array(data, pos)

        if typeName == 'Int64Array':
            return DataObject.ParseInt64Array(data, pos)
        if typeName == 'Uint64Array':
            return DataObject.ParseUint64Array(data, pos)
