class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero = 0
        for x in nums:
            if x != 0:
                nums[nonzero] = x
                nonzero += 1
        for i in range(nonzero, len(nums)):
            nums[i] = 0
