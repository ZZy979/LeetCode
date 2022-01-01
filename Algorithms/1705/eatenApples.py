import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        q = []
        ans = 0
        for i, (m, d) in enumerate(zip(apples, days)):
            while q and q[0][0] <= i:
                heapq.heappop(q)
            if m > 0:
                heapq.heappush(q, [i + d, m])
            if q:
                q[0][1] -= 1
                ans += 1
                if q[0][1] == 0:
                    heapq.heappop(q)
        
        i = len(apples)
        while q:
            while q and q[0][0] <= i:
                heapq.heappop(q)
            if q:
                d, m = heapq.heappop(q)
                eat = min(d - i, m)
                ans += eat
                i += eat
        return ans
