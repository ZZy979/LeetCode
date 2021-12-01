from collections import Counter

# 官方题解：双指针，时间复杂度O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        num = Counter()
        maxn = left = right = 0
        while right < n:
            num[s[right]] += 1
            maxn = max(maxn, num[s[right]])
            if right - left + 1 - maxn > k:
                num[s[left]] -= 1
                left += 1
            right += 1
        return right - left
