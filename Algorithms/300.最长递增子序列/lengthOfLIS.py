# 动态规划
# 时间复杂度O(n²)，空间复杂度O(n)
# 2324 ms
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = max((dp[j] for j in range(i) if nums[j] < nums[i]), default=0) + 1
        return max(dp)
