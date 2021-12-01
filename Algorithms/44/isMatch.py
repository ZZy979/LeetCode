class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]: s[:i]和p[:j]是否匹配
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
        return dp[m][n]
