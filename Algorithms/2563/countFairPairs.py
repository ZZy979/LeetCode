import bisect

# 排序+二分查找，时间复杂度O(nlog n)，空间复杂度O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            l = bisect.bisect_left(nums, lower - x, 0, i)
            r = bisect.bisect_right(nums, upper - x, 0, i)
            ans += r - l
        return ans
