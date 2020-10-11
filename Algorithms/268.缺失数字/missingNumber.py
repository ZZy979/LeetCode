class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        appear = [False] * (len(nums) + 1)
        for num in nums:
            appear[num] = True
        return appear.index(False)
