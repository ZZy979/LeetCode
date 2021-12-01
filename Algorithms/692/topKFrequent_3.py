import heapq
from collections import Counter

# 散列表+优先队列，时间复杂度O(nlog k)，空间复杂度O(n)
# 64 ms
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        for w, n in c.items():
            heapq.heappush(heap, Item(w, n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [heapq.heappop(heap).word for _ in range(k)]
        res.reverse()
        return res


class Item:
    
    def __init__(self, word, num):
        self.word = word
        self.num = num
    
    def __lt__(self, other):
        return self.num < other.num if self.num != other.num else self.word > other.word
