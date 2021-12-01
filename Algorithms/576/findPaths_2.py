# 官方题解：动态规划，116 ms
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        q = 10**9 + 7
        ans = 0
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % q
                            else:
                                ans = (ans + dp[i][j][k]) % q
        return ans
