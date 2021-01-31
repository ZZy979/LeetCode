# 官方题解2：并查集
# 时间复杂度O(n²log n)，空间复杂度O(n²)
# 268 ms
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        a = n * n
        index = [0] * a
        for r in range(n):
            for c in range(n):
                index[grid[r][c]] = r * n + c
        
        uf = UnionFind(a)
        for h in range(a):
            r, c = divmod(index[h], n)
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= h:
                    uf.union(index[h], nr * n + nc)
                if uf.find(0) == uf.find(a - 1):
                    return h


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
