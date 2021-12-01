class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        elif n == 0:
            return 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(s[0] == t[0])
        for i in range(1, n):
            dp[i][i] = dp[i - 1][i - 1] & (s[i] == t[i])
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + int(s[i] == t[0])
        for i in range(2, m):
            for j in range(1, min(i, n)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
