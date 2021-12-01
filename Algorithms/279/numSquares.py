import math

# 动态规划，时间复杂度O(n sqrt(n))
# 4104 ms
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, math.isqrt(n) + 1)]
        dp = [0x7fffffff] * (n + 1)
        dp[0] = 0
        for s in squares:
            for j in range(s, n + 1):
                dp[j] = min(dp[j], 1 + dp[j - s])
        return dp[-1]
