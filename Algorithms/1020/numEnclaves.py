from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for j in range(n):
            if grid[0][j] == 1:
                grid[0][j] = 0
                q.append((0, j))
            if grid[m - 1][j] == 1:
                grid[m - 1][j] = 0
                q.append((m - 1, j))
        for i in range(1, m - 1):
            if grid[i][0] == 1:
                grid[i][0] = 0
                q.append((i, 0))
            if grid[i][n - 1] == 1:
                grid[i][n - 1] = 0
                q.append((i, n - 1))

        while q:
            i, j = q.popleft()
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    q.append((ni, nj))
        return sum(sum(row) for row in grid)
