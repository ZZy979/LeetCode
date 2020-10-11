class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(self.subsets_from(nums, 0))
    
    def subsets_from(self, nums, k):
        if k == len(nums):
            yield []
        else:
            yield []
            for i in range(k, len(nums)):
                for subset in self.subsets_from(nums, i + 1):
                    yield [nums[i]] + subset
