class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for i in range(31, -1, -1):
            m |= (n & 1) << i
            n >>= 1
        return m
