class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                return i
            elif i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1
