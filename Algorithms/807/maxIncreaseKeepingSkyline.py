class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(grid[i]) for i in range(len(grid))]
        col_max = [max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        return sum(min(row_max[i], col_max[j]) - grid[i][j] for i in range(len(grid)) for j in range(len(grid[i])))
