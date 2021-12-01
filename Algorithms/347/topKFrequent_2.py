from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for num in nums:
            c[num] += 1
        q = []
        for num in c:
            heapq.heappush(q, (c[num], num))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        while q:
            ans.append(heapq.heappop(q)[1])
        return ans
