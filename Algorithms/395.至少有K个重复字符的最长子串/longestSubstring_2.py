from collections import Counter

# 官方题解：滑动窗口
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        n, res = len(s), 0
        for t in range(1, 27):
            count = Counter()
            l, r = 0, 0
            total, less = 0, 0
            while r < n:
                count[s[r]] += 1
                if count[s[r]] == 1:
                    total += 1
                    less += 1
                elif count[s[r]] == k:
                    less -= 1
                while total > t:
                    count[s[l]] -= 1
                    if count[s[l]] == k - 1:
                        less += 1
                    elif count[s[l]] == 0:
                        total -= 1
                        less -= 1
                    l += 1
                if less == 0:
                    res = max(res, r - l + 1)
                r += 1
        return res
