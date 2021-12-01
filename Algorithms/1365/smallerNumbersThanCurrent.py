class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = list(sorted(nums))
        return [sorted_nums.index(n) for n in nums]
