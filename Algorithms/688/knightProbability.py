class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[1] * n for _ in range(n)]
        for _ in range(k):
            dp = [
                [
                    sum(dp[r + dr][c + dc]
                        for dr, dc in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))
                        if 0 <= r + dr < n and 0 <= c + dc < n) / 8
                    for c in range(n)
                ] for r in range(n)
            ]
        return dp[row][column]
