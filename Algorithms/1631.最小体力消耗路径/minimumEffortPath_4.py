# 官方题解3：最短路径Dijkstra
# 时间复杂度O(mnlog mn)，空间复杂度O(mn)
# 1028 ms
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        dist = [0] + [float("inf")] * (m * n - 1)
        seen = set()
        while q:
            d, x, y = heapq.heappop(q)
            iden = x * n + y
            if iden in seen:
                continue
            if (x, y) == (m - 1, n - 1):
                break
            seen.add(iden)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n and max(d, abs(heights[x][y] - heights[nx][ny])) <= dist[nx * n + ny]:
                    dist[nx * n + ny] = max(d, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(q, (dist[nx * n + ny], nx, ny))
        return dist[m * n - 1]
