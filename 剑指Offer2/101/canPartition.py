class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [True] + [False] * target
        for x in nums:
            for j in range(target, x - 1, -1):
                dp[j] |= dp[j - x]
        return dp[target]
