class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # 方格i -> 三角2i, 2i+1
        # /或空格：左上三角2i、右下三角2i+1；\：右上三角2i、左下三角2i+1
        uf = UnionFind(2 * n * n)
        for r in range(n):
            for c in range(n):
                i = r * n + c
                if grid[r][c] == ' ':
                    uf.union(2 * i, 2 * i + 1)
                if r > 0:
                    uf.union(2 * (i - n) + 1, 2 * i)
                if c > 0:
                    b = 2 * i + 1 if grid[r][c] == '\\' else 2 * i
                    a = 2 * (i - 1) if grid[r][c - 1] == '\\' else 2 * (i - 1) + 1
                    uf.union(a, b)
        return sum(1 for i in range(2 * n * n) if uf.find(i) == i)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
