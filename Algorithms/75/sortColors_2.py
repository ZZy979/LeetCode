# 单指针+两次遍历，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        for i in range(p, n):
            if nums[i] == 1:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
