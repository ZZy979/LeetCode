import heapq

# 官方题解：最短路径Dijkstra，时间复杂度O(mnlog mn)，空间复杂度O(mn)
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        dist[0][0] = 0
        q = []
        heapq.heappush(q, State(0, 0, 0))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            s = heapq.heappop(q)
            if visited[s.x][s.y]:
                continue
            if s.x == n - 1 and s.y == m - 1:
                break
            visited[s.x][s.y] = True
            for dx, dy in dirs:
                nx, ny = s.x + dx, s.y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if (d := max(dist[s.x][s.y], moveTime[nx][ny]) + (s.x + s.y) % 2 + 1) < dist[nx][ny]:
                    dist[nx][ny] = d
                    heapq.heappush(q, State(nx, ny, d))
        return dist[n - 1][m - 1]


class State:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis
