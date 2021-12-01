# 并查集，时间复杂度O(n²log n)，空间复杂度O(n)
# 56 ms
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(1, n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return sum(1 for i in range(n) if uf.find(i) == i)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
