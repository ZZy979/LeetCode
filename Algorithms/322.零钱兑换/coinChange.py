class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0x7fffffff] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for j in range(c, amount + 1):
                dp[j] = min(dp[j], 1 + dp[j - c])
        return -1 if dp[-1] == 0x7fffffff else dp[-1]
