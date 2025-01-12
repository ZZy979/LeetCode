from collections import Counter

# 滑动窗口
# 时间复杂度O(n+m)，空间复杂度O(C)
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        diff = Counter()
        for c in word2:
            diff[c] -= 1
        cnt = sum(v < 0 for v in diff.values())

        ans = 0
        left = right = 0
        while left < n:
            while right < n and cnt > 0:
                diff[word1[right]] += 1
                if diff[word1[right]] == 0:
                    cnt -= 1
                right += 1
            if cnt == 0:
                ans += n - right + 1
            diff[word1[left]] -= 1
            if diff[word1[left]] == -1:
                cnt += 1
            left += 1
        return ans
