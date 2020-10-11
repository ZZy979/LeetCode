class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n - 1):
            if s[i] == '0' and s[i + 1] == '1' or s[i] == '1' and s[i + 1] == '0':
                count += 1
                r = 1
                while i - r >= 0 and i + 1 + r < n and s[i - r] == s[i] and s[i + 1 + r] == s[i + 1]:
                    count += 1
                    r += 1
        return count
