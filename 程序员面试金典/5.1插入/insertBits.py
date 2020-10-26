class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        s = N & ((1 << i) - 1)
        N >>= i
        N &= (-1 << (j - i + 1))
        N |= M
        N <<= i
        N |= s
        return N
