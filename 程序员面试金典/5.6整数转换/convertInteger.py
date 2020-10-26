class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        d = A ^ B
        n = 0
        for i in range(32):
            n += d % 2
            d //= 2
        return n
