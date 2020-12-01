import bisect

# 方法1：直接使用bisect模块，时间复杂度O(log n)
# 44 ms
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [-1, -1] if left == right else [left, right - 1]
