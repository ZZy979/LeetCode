# 官方题解3：数学
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        q, r = divmod(n, 3)
        if r == 0:
            return 3 ** q
        elif r == 1:
            return 3 ** (q - 1) * 4
        else:
            return 3 ** q * 2
