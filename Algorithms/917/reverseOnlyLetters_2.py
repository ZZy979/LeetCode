class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        return ''.join(c if not c.isalpha() else letters.pop() for c in s)
