class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if uf.find(i) != uf.find(j) and is_similar(strs[i], strs[j]):
                    uf.union(i, j)
        return sum(1 for i in range(n) if uf.find(i) == i)


def is_similar(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            if diff > 2:
                break
    return diff == 0 or diff == 2


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
