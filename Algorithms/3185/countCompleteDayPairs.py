from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        d = Counter()
        for h in hours:
            ans += d[(24 - h % 24) % 24]
            d[h % 24] += 1
        return ans
