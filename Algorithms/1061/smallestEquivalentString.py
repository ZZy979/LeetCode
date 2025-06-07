class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for c1, c2 in zip(s1, s2):
            uf.union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        return ''.join(chr(ord('a') + uf.find(ord(c) - ord('a'))) for c in baseStr)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if a > b:
            a, b = b, a
        self.parent[b] = a
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
