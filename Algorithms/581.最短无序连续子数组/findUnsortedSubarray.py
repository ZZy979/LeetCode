class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        i, j = 0, n - 1
        while i < n and nums[i] == sorted_nums[i]:
            i += 1
        while j >= 0 and nums[j] == sorted_nums[j]:
            j -= 1
        return max(0, j - i + 1)
