class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        for e in edges:
            e[1] -= 1
            e[2] -= 1
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        ans = 0
        # 公共边
        for t, u, v in edges:
            if t == 3:
                used = False
                if alice_uf.find(u) != alice_uf.find(v):
                    alice_uf.union(u, v)
                    used = True
                if bob_uf.find(u) != bob_uf.find(v):
                    bob_uf.union(u, v)
                    used = True
                if not used:
                    ans += 1
        # 独占边
        for t, u, v in edges:
            if t == 1:
                if alice_uf.find(u) != alice_uf.find(v):
                    alice_uf.union(u, v)
                else:
                    ans += 1
            elif t == 2:
                if bob_uf.find(u) != bob_uf.find(v):
                    bob_uf.union(u, v)
                else:
                    ans += 1
        if sum(1 for v in range(n) if alice_uf.find(v) == v) > 1 \
            or sum(1 for v in range(n) if bob_uf.find(v) == v) > 1:
            return -1
        return ans


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
