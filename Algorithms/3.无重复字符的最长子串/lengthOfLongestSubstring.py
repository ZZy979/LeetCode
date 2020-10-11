class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        c = set()
        right = 0
        for left in range(len(s)):
            while right < len(s) and s[right] not in c:
                c.add(s[right])
                right += 1
            ans = max(ans, right - left)
            c.remove(s[left])
        return ans
