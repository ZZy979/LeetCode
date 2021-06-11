# 官方题解：背包问题
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        q = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp[i][0] = 1
        for earn, members in zip(profit, group):
            for j in range(n, members - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - members][max(0, k - earn)]) % q
        return dp[n][minProfit]
