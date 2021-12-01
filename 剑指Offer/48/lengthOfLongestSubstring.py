class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        left = ans = 0
        c = {}
        for right in range(n):
            if s[right] in c:
                left = max(left, c[s[right]] + 1)
            ans = max(ans, right - left + 1)
            c[s[right]] = right
        return ans
