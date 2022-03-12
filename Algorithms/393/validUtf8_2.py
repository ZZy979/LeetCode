class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            b = get_bytes(data[i])
            if b == -1 or i + b > n or any(data[j] & 0xc0 != 0x80 for j in range(i + 1, i + b)):
                return False
            i += b
        return True


def get_bytes(num):
    if (num & 0x80) == 0:
        return 1
    elif (num & 0xe0) == 0xc0:
        return 2
    elif (num & 0xf0) == 0xe0:
        return 3
    elif (num & 0xf8) == 0xf0:
        return 4
    else:
        return -1
