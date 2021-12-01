import heapq

# 官方题解：堆+贪心
# 时间复杂度O((n+k)log n)，空间复杂度O(n)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        n = len(profits)
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        q = []
        cur = 0
        for _ in range(k):
            while cur < n and projects[cur][0] <= w:
                heapq.heappush(q, -projects[cur][1])
                cur += 1
            if q:
                w += -heapq.heappop(q)
            else:
                break
        return w
