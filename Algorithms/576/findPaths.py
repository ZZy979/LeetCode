# 动态规划，164 ms
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] += 1
            dp[-1][j] += 1
        for i in range(m):
            dp[i][0] += 1
            dp[i][-1] += 1
        
        q = 10**9 + 7
        ans = dp[startRow][startColumn]
        for k in range(2, maxMove + 1):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i >= 1:
                        new_dp[i][j] += dp[i - 1][j]
                    if i < m - 1:
                        new_dp[i][j] += dp[i + 1][j]
                    if j >= 1:
                        new_dp[i][j] += dp[i][j - 1]
                    if j < n - 1:
                        new_dp[i][j] += dp[i][j + 1]
                    new_dp[i][j] %= q
            dp = new_dp
            ans = (ans + dp[startRow][startColumn]) % q
        return ans
