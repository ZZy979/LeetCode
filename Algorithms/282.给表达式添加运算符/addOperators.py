# 回溯，7680 ms
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        nums = [''] * (2 * len(num) - 1)
        nums[::2] = num
        self.backtrack(nums, 1, 0, target)
        return self.ans

    def backtrack(self, nums, start, num_start, target):
        if start >= len(nums):
            expr = ''.join(nums)
            if eval(expr) == target:
                self.ans.append(expr)
            return
        for i in range(start, len(nums) + 2, 2):
            if i == len(nums):
                self.backtrack(nums, i, num_start, target)
            else:
                for op in '+-*':
                    nums[i] = op
                    self.backtrack(nums, i + 2, i + 1, target)
                    nums[i] = ''
                if nums[num_start] == '0':
                    break
