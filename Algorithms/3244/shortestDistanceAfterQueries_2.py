# 官方题解：贪心，时间复杂度O(n+q)，空间复杂度O(n)
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        roads = [i + 1 for i in range(n)]  # roads[u] = v表示最短路径包含道路(u, v)
        res = []
        dist = n - 1
        for u, v in queries:
            k, roads[u] = roads[u], v
            while k != -1 and k < v:
                roads[k], k = -1, roads[k]
                dist -= 1
            res.append(dist)
        return res
