# 方法1：动态规划，dp[i][j]: 使用前i种硬币表示j分的方法数
# 1628 ms
class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
                dp[j] %= 1000000007
        return dp[-1]
