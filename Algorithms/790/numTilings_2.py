# 官方题解：动态规划
class Solution:
    def numTilings(self, n: int) -> int:
        # dp[i]表示前i-1列都被覆盖，第i列两个都没覆盖、只覆盖上面、只覆盖下面和两个都覆盖的方法数
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][3] = 1
        q = 10**9 + 7
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % q
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % q
            dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % q
        return dp[n][3]
