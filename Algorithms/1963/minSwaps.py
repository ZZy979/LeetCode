# 贪心+双指针
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        s = list(s)
        left, right = 0, n - 1
        ans = unmatched = 0
        while left < right:
            unmatched += 1 if s[left] == ']' else -1
            if unmatched > 0:
                while s[right] == ']':
                    right -= 1
                s[left], s[right] = s[right], s[left]
                ans += 1
                unmatched -= 2
            left += 1
        return ans
