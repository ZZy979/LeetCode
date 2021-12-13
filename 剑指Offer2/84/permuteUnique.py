class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.permutaions(nums, 0)
        return self.ans
    
    def permutaions(self, nums, k):
        if k == len(nums):
            self.ans.append(nums.copy())
            return
        seen = set()
        for i in range(k, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[k], nums[i] = nums[i], nums[k]
            self.permutaions(nums, k + 1)
            nums[k], nums[i] = nums[i], nums[k]
