class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f[i] = cost[i] + min{f[i + 1], f[i + 2]}
        f = [0] * len(cost)
        f[-2:] = cost[-2:]
        for i in range(len(cost) - 3, -1, -1):
            f[i] = cost[i] + min(f[i + 1], f[i + 2])
        return min(f[0], f[1])
