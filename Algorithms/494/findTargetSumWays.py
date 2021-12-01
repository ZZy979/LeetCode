# 官方题解：背包问题
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        diff = s - target
        if diff < 0 or diff % 2 != 0:
            return 0
        neg = diff // 2
        dp = [0] * (neg + 1)
        dp[0] = 1
        for x in nums:
            for j in range(neg, x - 1, -1):
                dp[j] += dp[j - x]
        return dp[neg]
