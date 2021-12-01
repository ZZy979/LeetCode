# 官方题解1：动态规划
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[n - 1] > 0
