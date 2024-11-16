class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        # dp[i][j]表示将cuts[i]到cuts[j]之间的木棍全部切开的最小成本
        dp = [[0] * m for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(i + 2, m):
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]
        return dp[0][m - 1]
