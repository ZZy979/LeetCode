class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        dist = [0x7fffffff] * n
        dijkstra(graph, dist, k - 1)
        return -1 if (t := max(dist)) == 0x7fffffff else t


def dijkstra(graph, dist, src):
    n = len(graph)
    visited = [False] * n
    dist[src] = 0
    while True:
        u = min((i for i in range(n) if not visited[i]), key=dist.__getitem__, default=-1)
        if u == -1:
            break
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v] and (d := dist[u] + w) < dist[v]:
                dist[v] = d
