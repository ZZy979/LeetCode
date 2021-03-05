# 官方题解1：动态规划
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = max(max(j * (i - j), j * dp[i - j]) for j in range(1, i))
        return dp[n]
