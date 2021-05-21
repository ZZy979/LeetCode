import heapq
from collections import Counter

# 散列表+排序，时间复杂度O((n-k)log k)，空间复杂度O(n)
# 64 ms
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [w for w, _ in heapq.nsmallest(k, Counter(words).items(), key=lambda t: (-t[1], t[0]))]
