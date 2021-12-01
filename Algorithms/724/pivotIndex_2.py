class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if 2 * left_sum + nums[i] == total:
                return i
            left_sum += nums[i]
        return -1
