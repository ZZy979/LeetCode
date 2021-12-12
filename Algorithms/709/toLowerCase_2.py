class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(x | 32) if 65 <= (x := ord(c)) <= 90 else c for c in s)
