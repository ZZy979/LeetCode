from collections import defaultdict, deque

# BFS，时间复杂度O(n²+m²)，空间复杂度O(n+m)
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        g1 = build_graph(edges1)
        g2 = build_graph(edges2)
        t = max(bfs(g2, i, k - 1) for i in range(m))
        return [bfs(g1, i, k) + t for i in range(n)]

def build_graph(edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g

# 返回图g中与节点s的距离<=k的目标节点数
def bfs(g, s, k):
    q = deque([s])
    visited = set()
    for i in range(k + 1):
        for j in range(len(q)):
            u = q.popleft()
            visited.add(u)
            for v in g[u]:
                if v not in visited:
                    q.append(v)
    return len(visited)
