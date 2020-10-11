class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        p = 1 << 31
        while n:
            m += n % 2 * p
            p >>= 1
            n >>= 1
        return m
