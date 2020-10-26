class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        return N & ~(((1 << (j - i + 1)) - 1) << i) | (M << i)
