class Solution:
    def waysToStep(self, n: int) -> int:
        if n <= 2:
            return n
        elif n == 3:
            return 4
        dp = [0] * (n + 1)
        dp[1:4] = [1, 2, 4]
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
        return dp[n]
