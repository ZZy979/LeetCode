# 方法1：并查集
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n + 1)
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if grid[i][j] == '0':
                    uf.union(m * n, idx)
                else:
                    if j < n - 1 and grid[i][j + 1] == '1':
                        uf.union(idx, idx + 1)
                    if i < m - 1 and grid[i + 1][j] == '1':
                        uf.union(idx, idx + n)
        return sum(1 for i in range(m * n) if uf.find(i) == i)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
