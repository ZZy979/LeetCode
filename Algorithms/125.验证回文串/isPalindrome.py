class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        chars = [c for c in s.lower() if c.isalnum()]
        p, q = 0, len(chars) - 1
        while p < q:
            if chars[p] != chars[q]:
                return False
            p += 1
            q -= 1
        return True
