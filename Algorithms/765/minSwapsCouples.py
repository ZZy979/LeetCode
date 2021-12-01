from collections import Counter

# 官方题解：并查集
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 48 ms
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = UnionFind(n // 2)
        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)
        c = Counter()
        for i in range(n // 2):
            c[uf.find(i)] += 1
        return sum(v - 1 for k, v in c.items())


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
