class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, ans = 0, nums[0]
        for x in nums:
            pre = max(pre, 0) + x
            ans = max(ans, pre)
        return ans
