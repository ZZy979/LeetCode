class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        row = [None] * 10001
        col = [None] * 10001
        for i, (r, c) in enumerate(stones):
            if row[r] is None:
                row[r] = i
            if col[c] is None:
                col[c] = i
        for i, (r, c) in enumerate(stones):
            uf.union(row[r], i)
            uf.union(col[c], i)
        return sum(1 for i in range(n) if uf.find(i) != i)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
