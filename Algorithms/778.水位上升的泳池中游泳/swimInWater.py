from collections import deque

# 官方题解1(1)：二分查找+BFS
# 时间复杂度O(n²log n)，空间复杂度O(n²)
# 224 ms
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left, right = 0, n * n - 1
        while left < right:
            mid = (left + right) // 2
            if grid[0][0] <= mid and bfs(grid, mid):
                right = mid
            else:
                left = mid + 1
        return left


def bfs(grid, t):
    n = len(grid)
    q = deque([(0, 0)])
    visited = {(0, 0)}
    while q:
        r, c = q.popleft()
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= t:
                if nr == nc == n - 1:
                    return True
                q.append((nr, nc))
                visited.add((nr, nc))
    return False
