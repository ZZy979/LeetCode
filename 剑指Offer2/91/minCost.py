class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = costs[0]
        for i in range(1, n):
            dp = [min(dp[k] for k in range(3) if k != j) + costs[i][j] for j in range(3)]
        return min(dp)
