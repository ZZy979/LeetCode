from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and not visited[r][c]:
                    max_area = max(max_area, bfs(grid, visited, r, c))
        return max_area


def bfs(grid, visited, r, c):
    visited[r][c] = True
    area = 0
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        area += 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
    return area
