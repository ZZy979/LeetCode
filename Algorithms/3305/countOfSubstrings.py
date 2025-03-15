from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        for i in range(n - k - 4):
            cnt = Counter()
            for j in range(i, n):
                cnt[word[j] if word[j] in 'aeiou' else 'x'] += 1
                if all(cnt[c] > 0 for c in 'aeiou') and cnt['x'] == k:
                    ans += 1
        return ans
