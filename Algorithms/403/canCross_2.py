# 官方题解：动态规划，时间复杂度O(n²)
# 1164 ms
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if any(stones[i] - stones[i - 1] > i for i in range(1, n)):
            return False
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True
        return False
