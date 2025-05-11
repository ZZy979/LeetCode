# 动态规划，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        # dp[i][0]表示平铺2*i面板的方法数
        # dp[i][1]表示平铺2*i且左上角被占据的面板的方法数
        dp = [[0, 0]] * (n + 1)
        dp[1:4] = [[1, 0], [2, 1], [5, 2]]
        q = 10**9 + 7
        for i in range(4, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % q
            dp[i][1] = (dp[i - 1][1] + dp[i - 2][0]) % q
        return dp[n][0]
