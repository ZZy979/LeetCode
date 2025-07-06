# 排序+滑动窗口，时间复杂度O(nlog n)，空间复杂度O(1)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = ans = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                ans = max(ans, right - left + 1)
        return ans
