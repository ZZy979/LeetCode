class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        i = ans = 0
        while i < n:
            c = s[i]
            m = 1
            i += 1
            while m > 0:
                m += 1 if s[i] == c else -1
                i += 1
            ans += 1
        return ans
