from collections import Counter

# 散列表，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter()
        ans = 0
        for w in words:
            r = w[1] + w[0]
            if cnt[r] > 0:
                cnt[r] -= 1
                ans += 4
            else:
                cnt[w] += 1
        if any(w[0] == w[1] and n > 0 for w, n in cnt.items()):
            ans += 2
        return ans
