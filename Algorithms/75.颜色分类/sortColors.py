from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        for c in range(3):
            for j in range(count[c]):
                nums[i] = c
                i += 1
