class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        dp = [[0] * (s // 2 + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, s // 2 + 1):
                dp[i][j] = dp[i - 1][j]
                if stones[i - 1] <= j:
                    dp[i][j] = max(dp[i][j], stones[i - 1] + dp[i - 1][j - stones[i - 1]])
        return s - 2 * dp[-1][-1]
