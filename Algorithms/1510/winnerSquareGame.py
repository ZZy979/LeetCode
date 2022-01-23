import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        # dp[i]: 轮到Alice，剩i个石子，Alice是否能赢
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - j ** 2] for j in range(1, math.isqrt(i) + 1))
        return dp[n]
