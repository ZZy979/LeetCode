class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.backtrack(s, 0, [])
        return self.ans
    
    def backtrack(self, s, start, substrs):
        if start == len(s):
            self.ans.append(substrs.copy())
        for i in range(start, len(s)):
            if is_palindrome(s[start:i + 1]):
                substrs.append(s[start:i + 1])
                self.backtrack(s, i + 1, substrs)
                substrs.pop()


def is_palindrome(s):
    return s == s[::-1]
