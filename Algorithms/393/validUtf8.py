class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            if (data[i] & 0x80) == 0:
                # 1字节
                i += 1
            elif (data[i] & 0xe0) == 0xc0:
                # 2字节
                if i + 1 >= n or (data[i + 1] & 0xc0) != 0x80:
                    return False
                i += 2
            elif (data[i] & 0xf0) == 0xe0:
                # 3字节
                if i + 2 >= n or (data[i + 1] & 0xc0) != 0x80 or (data[i + 2] & 0xc0) != 0x80:
                    return False
                i += 3
            elif (data[i] & 0xf8) == 0xf0:
                # 4字节
                if i + 3 >= n or (data[i + 1] & 0xc0) != 0x80 or (data[i + 2] & 0xc0) != 0x80 or (data[i + 3] & 0xc0) != 0x80:
                    return False
                i += 4
            else:
                return False
        return True
