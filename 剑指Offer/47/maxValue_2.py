class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j] = max(dp[j], dp[j - 1]) + grid[i - 1][j - 1]
        return dp[n]
