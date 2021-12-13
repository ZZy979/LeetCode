class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        visited, border = set(), set()
        dfs(grid, visited, row, col, border)
        for r, c in border:
            grid[r][c] = color
        return grid


def dfs(grid, visited, r, c, border):
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == grid[r][c]):
            border.add((r, c))
    visited.add((r, c))
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == grid[r][c] and (nr, nc) not in visited:
            dfs(grid, visited, nr, nc, border)
