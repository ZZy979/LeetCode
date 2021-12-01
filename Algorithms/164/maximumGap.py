# 方法1：直接排序
# 时间复杂度O(nlog n)，空间复杂度O(1)
# 48 ms
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(nums[i + 1] - nums[i] for i in range(len(nums) - 1))
