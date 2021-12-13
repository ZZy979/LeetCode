import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        q = []
        for x, n in c.items():
            heapq.heappush(q, (n, x))
            if len(q) > k:
                heapq.heappop(q)
        return [heapq.heappop(q)[1] for _ in range(len(q))]
