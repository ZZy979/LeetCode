class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                s[i] = next(c for c in 'abc' if (i == 0 or c != s[i - 1]) and (i == len(s) - 1 or s[i + 1] == '?' or c != s[i + 1]))
        return ''.join(s)
