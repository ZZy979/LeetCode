# DFS，超时。。
class Solution:
    def __init__(self):
        self.visited = set()
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for hr, hc in hits:
            if grid[hr][hc] == 0:
                ans.append(0)
            else:
                grid[hr][hc] = 0
                drop = 0
                for dr, dc in self.directions:
                    self.visited.clear()
                    nr, nc = hr + dr, hc + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        if not self.stable(grid, nr, nc):
                            drop += len(self.visited)
                            for r, c in self.visited:
                                grid[r][c] = 0
                ans.append(drop)
        return ans

    def stable(self, grid, r, c):
        if r == 0:
            return True
        self.visited.add((r, c))
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 1 and (nr, nc) not in self.visited and self.stable(grid, nr, nc):
                return True
        return False
