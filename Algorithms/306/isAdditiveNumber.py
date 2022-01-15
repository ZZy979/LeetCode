class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtrack(num, 0, [])
    
    def backtrack(self, s, start, nums):
        if start >= len(s):
            return len(nums) >= 3
        if s[start] == '0':
            return (len(nums) < 2 or nums[-1] == nums[-2] == 0) and self.backtrack(s, start + 1, nums + [0])
        else:
            return any(self.backtrack(s, i, nums + [int(s[start:i])]) for i in range(start + 1, len(s) + 1) if len(nums) < 2 or int(s[start:i]) == nums[-1] + nums[-2])
