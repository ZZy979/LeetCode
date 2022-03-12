class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        b = 0
        for num in data:
            if b > 0:
                if (num >> 6) != 2:
                    return False
                b -= 1
            elif num >> 7 == 0:
                b = 0
            elif num >> 5 == 0b110:
                b = 1
            elif num >> 4 == 0b1110:
                b = 2
            elif num >> 3 == 0b11110:
                b = 3
            else:
                return False
        return b == 0
