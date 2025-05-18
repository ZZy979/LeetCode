from collections import Counter
from sortedcontainers import SortedSet

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ans = SortedSet()
        for d1 in (0, 2, 4, 6, 8):
            if cnt[d1] > 0:
                cnt[d1] -= 1
                for d3 in range(1, 10):
                    if cnt[d3] > 0:
                        cnt[d3] -= 1
                        for d2 in range(10):
                            if cnt[d2] > 0:
                                ans.add(d3 * 100 + d2 * 10 + d1)
                        cnt[d3] += 1
                cnt[d1] += 1
        return list(ans)
