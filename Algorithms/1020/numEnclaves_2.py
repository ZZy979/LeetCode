class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for j in range(n):
            if grid[0][j] == 1:
                dfs(grid, visited, 0, j)
            if grid[m - 1][j] == 1:
                dfs(grid, visited, m - 1, j)
        for i in range(1, m - 1):
            if grid[i][0] == 1:
                dfs(grid, visited, i, 0)
            if grid[i][n - 1] == 1:
                dfs(grid, visited, i, n - 1)
        return sum(grid[i][j] == 1 and not visited[i][j] for i in range(m) for j in range(n))


def dfs(grid, visited, r, c):
    visited[r][c] = True
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 1 and not visited[nr][nc]:
            dfs(grid, visited, nr, nc)
