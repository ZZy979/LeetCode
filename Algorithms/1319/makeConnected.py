# 并查集
# 时间复杂度O(mα(n))，空间复杂度O(n)，α是阿克曼函数的反函数
# 188 ms
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a, b)
        return sum(1 for v in range(n) if uf.find(v) == v) - 1


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
