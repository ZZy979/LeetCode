# 官方题解3：动态规划
# 时间复杂度O(km)，空间复杂度O(n)
# 44 ms
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(k):
            nxt = [0 for _ in range(n + 1)]
            for u, v in relation:
                nxt[v] += dp[u]
            dp = nxt
        return dp[n - 1]
