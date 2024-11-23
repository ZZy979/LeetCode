from collections import deque

# 方法一：BFS，时间复杂度O(q(n+q))，空间复杂度O(n+q)
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[i + 1] for i in range(n)]
        graph[-1] = []
        ans = []
        for u, v in queries:
            graph[u].append(v)
            ans.append(bfs(graph, 0, n - 1))
        return ans

def bfs(graph, start, end):
    visited = {start}
    dist = 0
    q = deque([start])
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            if u == end:
                return dist
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        dist += 1
    return -1
