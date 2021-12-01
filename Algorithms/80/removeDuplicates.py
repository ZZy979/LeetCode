class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        q = 1
        for p in range(2, n):
            if nums[p] > nums[q] or nums[p] > nums[q - 1]:
                q += 1
                nums[q] = nums[p]
        return q + 1
