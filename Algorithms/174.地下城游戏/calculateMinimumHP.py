class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[99999999] * n for r in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if c < n - 1:
                    dp[r][c] = min(dp[r][c], max(1, dp[r][c + 1] - dungeon[r][c]))
                if r < m - 1:
                    dp[r][c] = min(dp[r][c], max(1, dp[r + 1][c] - dungeon[r][c]))
        return dp[0][0]
