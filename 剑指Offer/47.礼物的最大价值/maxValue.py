class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + grid[i][j])
                if j < n - 1:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + grid[i][j])
        return dp[0][0]
