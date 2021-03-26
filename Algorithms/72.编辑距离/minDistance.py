class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        dp[0] = list(range(n + 1))
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0))
        return dp[m][n]
