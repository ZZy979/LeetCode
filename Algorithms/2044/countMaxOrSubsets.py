class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_val, self.ans = 0, 0
        self.backtrack(nums, 0, 0)
        return self.ans
    
    def backtrack(self, nums, start, or_val):
        if start >= len(nums):
            if or_val > self.max_val:
                self.max_val, self.ans = or_val, 1
            elif or_val == self.max_val:
                self.ans += 1
            return
        self.backtrack(nums, start + 1, or_val | nums[start])
        self.backtrack(nums, start + 1, or_val)
