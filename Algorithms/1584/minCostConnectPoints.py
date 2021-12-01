class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        graph = calc_dists(points)
        return prim(graph)


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def calc_dists(points):
    n = len(points)
    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dists[i][j] = dists[j][i] = dist(*points[i], *points[j])
    return dists


def prim(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    dist = graph[0]
    ans = 0
    while True:
        v, min_dist = -1, 0x7fffffff
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                v, min_dist = i, dist[i]
        if v == -1:
            break
        visited[v] = True
        ans += dist[v]
        for i in range(n):
            if not visited[i] and graph[v][i] < dist[i]:
                dist[i] = graph[v][i]
    return ans
