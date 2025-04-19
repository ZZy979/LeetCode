# 排序+双指针，时间复杂度O(nlog n)，空间复杂度O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        left = right = len(nums)
        for i, x in enumerate(nums):
            while left > 0 and nums[left - 1] >= lower - x:
                left -= 1
            while right > 0 and nums[right - 1] > upper - x:
                right -= 1
            ans += min(right, i) - min(left, i)
        return ans
