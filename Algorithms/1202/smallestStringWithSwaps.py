from collections import defaultdict

# 并查集+排序
# 856 ms
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
        
        components_idx = defaultdict(list)
        ans = list(s)
        for i in range(n):
            components_idx[uf.find(i)].append(i)
        for i in components_idx:
            components_idx[i].sort()
            component = [ans[i] for i in components_idx[i]]
            component.sort()
            for k, c in zip(components_idx[i], component):
                ans[k] = c
        return ''.join(ans)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
