import heapq

# 官方题解：扫描线+优先队列
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        boundaries = []
        for left, right, _ in buildings:
            boundaries.append(left)
            boundaries.append(right)
        boundaries.sort()

        ans = []
        q = []
        n, idx = len(buildings), 0
        for b in boundaries:
            while idx < n and buildings[idx][0] <= b:
                heapq.heappush(q, Building(buildings[idx][1], buildings[idx][2]))
                idx += 1
            while q and q[0].right <= b:
                heapq.heappop(q)
            maxn = 0 if not q else q[0].hight
            if not ans or maxn != ans[-1][1]:
                ans.append([b, maxn])
        return ans


class Building:

    def __init__(self, right, hight):
        self.right = right
        self.hight = hight
    
    def __lt__(self, other):
        return self.hight > other.hight
