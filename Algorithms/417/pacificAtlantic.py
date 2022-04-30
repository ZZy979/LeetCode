from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_reachable = bfs(heights, {(0, c) for c in range(n)} | {(r, 0) for r in range(1, m)})
        atlantic_reachable = bfs(heights, {(m - 1, c) for c in range(n)} | {(r, n - 1) for r in range(m - 1)})
        return list(map(list, pacific_reachable & atlantic_reachable))


def bfs(heights, start):
    m, n = len(heights), len(heights[0])
    q = deque(start)
    visited = start
    while q:
        r, c = q.popleft()
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    return visited
