class Solution:
    def maxPower(self, s: str) -> int:
        ans = m = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                m += 1
            else:
                ans = max(ans, m)
                m = 1
        ans = max(ans, m)
        return ans
