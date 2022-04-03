class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0
