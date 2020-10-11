class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        q = 0
        for p in range(1, len(nums)):
            if nums[p] > nums[q]:
                q += 1
                nums[q] = nums[p]
        del nums[q + 1:]
        return q + 1
