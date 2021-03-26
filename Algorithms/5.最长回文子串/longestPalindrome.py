# 中心扩展法，时间复杂度O(n²)，空间复杂度O(1)
# 1024 ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            left1, right1 = expand_center(s, i, i)
            left2, right2 = expand_center(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


def expand_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1
