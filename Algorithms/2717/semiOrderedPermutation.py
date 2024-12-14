class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(1)
        j = nums.index(n)
        return i + n - 1 - j if i < j else i + n - 2 - j
