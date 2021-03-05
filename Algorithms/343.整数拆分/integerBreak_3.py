# 官方题解2：优化的动态规划（需要数学证明）
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        return dp[n]
