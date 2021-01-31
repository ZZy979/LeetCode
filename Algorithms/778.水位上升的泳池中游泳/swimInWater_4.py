# 官方题解3：Dijkstra算法
# 时间复杂度O(n²log n)，空间复杂度O(n²)
# 112 ms
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        # dist[r][c]: 到(r, c)需要等待的最少时间
        dist = [[n * n] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        while heap:
            h, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == c == n - 1:
                return dist[n - 1][n - 1]
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and max(dist[r][c], grid[nr][nc]) < dist[nr][nc]:
                    dist[nr][nc] = max(dist[r][c], grid[nr][nc])
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
