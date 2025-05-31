from collections import defaultdict, deque

# 拓扑排序+动态规划，时间复杂度O((n+m)C)，空间复杂度O(nC+m)，其中C=26
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        # 邻接表
        g = defaultdict(list)
        # 节点的入度统计，用于找出拓扑排序中最开始的节点
        indeg = [0] * n
        for x, y in edges:
            indeg[y] += 1
            g[x].append(y)

        # 记录拓扑排序过程中遇到的节点个数
        # 如果最终 found 的值不为 n，说明图中存在环
        found = 0
        f = [[0] * 26 for _ in range(n)]  # f(v,c)表示以节点v为终点的所有路径中，包含颜色c的节点数量的最大值
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            found += 1
            u = q.popleft()
            # 将节点 u 对应的颜色增加 1
            f[u][ord(colors[u]) - ord('a')] += 1
            # 枚举 u 的后继节点 v
            for v in g[u]:
                indeg[v] -= 1
                # 将 f(v,c) 更新为其与 f(u,c) 的较大值
                for c in range(26):
                    f[v][c] = max(f[v][c], f[u][c])
                if indeg[v] == 0:
                    q.append(v)

        if found != n:
            return -1
        return max(max(r) for r in f)
