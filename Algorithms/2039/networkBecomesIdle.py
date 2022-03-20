# Dijkstra算法：超时
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # 假设服务器i与服务器0之间的最短路径长度为l，patience[i]=p
        # 则服务器i在前2l秒发送n=ceil(2l/p)条消息，之后(n-1)p+1秒收到所有回复
        n = len(patience)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dist = dijkstra(graph)
        return max(2 * dist[i] + (math.ceil(2 * dist[i] / patience[i]) - 1) * patience[i] + 1 for i in range(1, n))


def dijkstra(graph):
    n = len(graph)
    dist = [0x7fffffff] * n
    dist[0] = 0
    visited = [False] * n
    for _ in range(n - 1):
        u = min((i for i in range(n) if not visited[i]), key=dist.__getitem__)
        visited[u] = True
        for v in graph[u]:
            if not visited[v] and (d := dist[u] + 1) < dist[v]:
                dist[v] = d
    return dist
