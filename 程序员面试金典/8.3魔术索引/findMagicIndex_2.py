class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1
