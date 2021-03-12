# 回溯法（超时）
class Solution:
    def minCut(self, s: str) -> int:
        self.ans = len(s) - 1
        self.backtrack(s, 0)
        return self.ans
    
    def backtrack(self, s, split):
        if is_palindrome(s):
            self.ans = min(self.ans, split)
        for i in range(len(s) - 1, 0, -1):
            if is_palindrome(s[:i]):
                self.backtrack(s[i:], split + 1)


def is_palindrome(s):
    return s == s[::-1]
