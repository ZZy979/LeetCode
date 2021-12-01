class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(arrLen, steps // 2 + 1)
        dp = [0] * n
        dp[0] = 1
        q = 10**9 + 7
        for j in range(1, steps + 1):
            dp2 = [((dp[i - 1] if i > 0 else 0) + dp[i] + (dp[i + 1] if i < n - 1 else 0)) % q for i in range(n)]
            dp = dp2
        return dp[0]
