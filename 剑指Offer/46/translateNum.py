# 回溯，32 ms
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        self.ans = 0
        self.backtrack(num, 0)
        return self.ans
    
    def backtrack(self, num, start):
        if start >= len(num):
            self.ans += 1
            return
        self.backtrack(num, start + 1)
        if start < len(num) - 1 and 10 <= int(num[start:start + 2]) <= 25:
            self.backtrack(num, start + 2)
