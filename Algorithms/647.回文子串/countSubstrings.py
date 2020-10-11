class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            count += 1
            r = 1
            while i - r >= 0 and i + r < n and s[i - r] == s[i + r]:
                count += 1
                r += 1
            if i < n - 1 and s[i] == s[i + 1]:
                count += 1
                r = 1
                while i - r >= 0 and i + r < n - 1 and s[i - r] == s[i + 1 + r]:
                    count += 1
                    r += 1
        return count
