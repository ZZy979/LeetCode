from itertools import accumulate

# 超时
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        presum = list(accumulate(stoneValue, initial=0))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # dp[i][j]: [i, j)对应的最大得分
        for r in range(2, n + 1):
            for i in range(n + 1 - r):
                j = i + r
                for k in range(i + 1, j):
                    left = presum[k] - presum[i]
                    right = presum[j] - presum[k]
                    score = left + dp[i][k] if left < right else right + dp[k][j] if right < left else left + max(dp[i][k], dp[k][j])
                    dp[i][j] = max(dp[i][j], score)
        return dp[0][n]
