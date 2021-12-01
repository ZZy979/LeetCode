# 方法2：排序
# 时间复杂度O(nlog n)，空间复杂度O(1)
# 52 ms
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
