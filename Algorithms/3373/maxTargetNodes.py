from collections import defaultdict

# DFS，时间复杂度O(n+m)，空间复杂度O(n+m)
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        color1, count1 = build(edges1)
        color2, count2 = build(edges2)
        return [count1[color1[i]] + max(count2) for i in range(n)]

def build(edges):
    n = len(edges) + 1
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    color = [0] * n
    even = dfs(g, 0, -1, 0, color)
    return color, [even, n - even]

# 返回图g中与node距离为偶数的目标节点数
def dfs(g, node, parent, depth, color):
    res = 1 - depth % 2
    color[node] = depth % 2
    for v in g[node]:
        if v == parent:
            continue
        res += dfs(g, v, node, depth + 1, color)
    return res
