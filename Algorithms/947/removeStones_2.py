class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for i, (r, c) in enumerate(stones):
            # uf.union(~r, c)
            # uf.union(r - 10001, c)
            uf.union(r + 10001, c)
        return len(stones) - uf.count


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa
            self.count -= 1
    
    def find(self, a):
        if a not in self.parent:
            self.parent[a] = a
            self.count += 1
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
