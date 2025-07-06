# 一次遍历，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans, last, count = 0, None, 1
        for c in word:
            if c == last:
                count += 1
            else:
                ans += count - 1
                last = c
                count = 1
        return ans + (count - 1) + 1
