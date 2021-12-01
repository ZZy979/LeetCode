class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        union_find = UnionFind(len(graph))
        for a in range(len(graph)):
            for i, b in enumerate(graph[a]):
                root_a = union_find.find(a)
                root_b = union_find.find(b)
                if root_a == root_b:
                    return False
                elif i > 0:
                    union_find.unite(graph[a][0], b)
        return True


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a
    
    def unite(self, a, b):
        self.parent[b] = a
