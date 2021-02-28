# 方法2：DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(grid, r, c)
        return count
    
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == '1':
                self.dfs(grid, nr, nc)
