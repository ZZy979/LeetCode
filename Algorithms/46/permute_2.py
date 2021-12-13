class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(nums, 0)
        return self.ans
    
    def backtrack(self, nums, start):
        if start == len(nums):
            self.ans.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.backtrack(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
