import heapq

# 官方题解：最小堆+DFS
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visited = [[False] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i * n + j))
        ans = 0
        while heap:
            h, p = heapq.heappop(heap)
            i, j = divmod(p, n)
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    ans += max(0, h - heightMap[ni][nj])
                    visited[ni][nj] = True
                    heapq.heappush(heap, (max(h, heightMap[ni][nj]), ni * n + nj))
        return ans
