class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_flips_row = sum(grid[i][k] != grid[i][n - 1 - k] for i in range(m) for k in range(n // 2))
        num_flips_col = sum(grid[k][j] != grid[m - 1 - k][j] for j in range(n) for k in range(m // 2))
        return min(num_flips_row, num_flips_col)
