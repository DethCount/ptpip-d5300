import struct

class PtpIpDataObject(object):
    """docstring for PtpIpDataObject"""
    def __init__(self, packet, data):
        super(PtpIpDataObject, self).__init__()
        self.packet = packet
        self.data = data

    def ParseUint8(data, pos):
        pos2 = pos + 1
        return (struct.unpack('B', data[pos:pos2])[0], pos2)

    def ParseUint16(data, pos):
        pos2 = pos + 2
        return (struct.unpack('H', data[pos:pos2])[0], pos2)

    def ParseUint32(data, pos):
        pos2 = pos + 4
        return (struct.unpack('I', data[pos:pos2])[0], pos2)

    def ParseString(data, pos):
        (length, pos) = PtpIpDataObject.ParseUint8(data, pos)

        s = ''
        for i in range(0, length):
            (c, pos) = PtpIpDataObject.ParseUint16(data, pos)
            s += chr(c)

        return (s, pos)

    def ParseArrayByLength(typeLength, data, pos):
        (length, pos) = PtpIpDataObject.ParseUint32(data, pos)

        results = []
        for i in range(0, length):
            pos2 = pos + typeLength
            results.append(data[pos:pos2])
            pos = pos2

        return (results, pos)

    def ParseArray(typeName, data, pos):
        (length, pos) = PtpIpDataObject.ParseUint32(data, pos)

        results = []
        for i in range(0, length):
            (item, pos) = PtpIpDataObject.ParseType(typeName, data, pos)
            results.append(item)

        return (results, pos)


    def ParseType(typeName, data, pos):
        if typeName == 'Uint8':
            return PtpIpDataObject.ParseUint8(data, pos)

        if typeName == 'Uint16':
            return PtpIpDataObject.ParseUint16(data, pos)

        if typeName == 'Uint32':
            return PtpIpDataObject.ParseUint32(data, pos)

        if typeName == 'String':
            return PtpIpDataObject.ParseString(data, pos)
