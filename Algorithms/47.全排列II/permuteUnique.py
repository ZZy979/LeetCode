class Solution:

    def __init__(self):
        self.ans = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.permutaions(nums, 0)
        return self.ans
    
    def permutaions(self, nums, k):
        if k == len(nums):
            self.ans.append(nums.copy())
        else:
            seen = set()
            for i in range(k, len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[k], nums[i] = nums[i], nums[k]
                    self.permutaions(nums, k + 1)
                    nums[k], nums[i] = nums[i], nums[k]
                    last = nums[i]
