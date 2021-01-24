# 官方题解1：深度优先搜索
# 时间复杂度O(n+m)，空间复杂度O(n+m)，m是connections的长度
# 128 ms
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        edges = collections.defaultdict(list)
        for a, b in connections:
            edges[a].append(b)
            edges[b].append(a)
        visited = set()
        ans = 0
        for v in range(n):
            if v not in visited:
                dfs(edges, visited, v)
                ans += 1
        return ans - 1


def dfs(edges, visited, u):
    visited.add(u)
    for v in edges[u]:
        if v not in visited:
            dfs(edges, visited, v)
