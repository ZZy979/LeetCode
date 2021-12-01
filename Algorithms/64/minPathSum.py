class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[99999999] * n for i in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r < m - 1:
                    dp[r][c] = min(dp[r][c], dp[r + 1][c] + grid[r][c])
                if c < n - 1:
                    dp[r][c] = min(dp[r][c], dp[r][c + 1] + grid[r][c])
        return dp[0][0]
