import heapq

# 官方题解1：最小堆
# 时间复杂度O(nmlog nm)，空间复杂度O(nm)
# 940 ms
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap = [1]
        for i in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                nxt = ugly * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return ugly
