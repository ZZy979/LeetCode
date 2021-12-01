# 官方题解1(2)：二分查找+DFS
# 时间复杂度O(n²log n)，空间复杂度O(n²)
# 184 ms
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left, right = 0, n * n - 1
        while left < right:
            mid = (left + right) // 2
            visited = {(0, 0)}
            if grid[0][0] <= mid and dfs(grid, visited, mid, 0, 0):
                right = mid
            else:
                left = mid + 1
        return left


def dfs(grid, visited, t, r, c):
    n = len(grid)
    visited.add((r, c))
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= t:
            if nr == nc == n - 1:
                return True
            if dfs(grid, visited, t, nr, nc):
                return True
    return False
