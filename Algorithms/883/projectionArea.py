class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        a_xy = sum(grid[i][j] != 0 for i in range(n) for j in range(n))
        a_yz = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        a_xz = sum(max(grid[i]) for i in range(n))
        return a_xy + a_yz + a_xz
