# 官方题解：动态规划
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houses = [c - 1 for c in houses]
        dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue
                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j0][k - 1])
                    if dp[i][j][k] != float("inf") and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float("inf") else ans
