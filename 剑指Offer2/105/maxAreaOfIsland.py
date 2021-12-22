class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                max_area = max(max_area, dfs(grid, r, c))
        return max_area


def dfs(grid, r, c):
    if grid[r][c] == 0:
        return 0
    grid[r][c] = 0
    area = 1
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
            area += dfs(grid, nr, nc)
    return area
