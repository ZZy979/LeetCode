from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        edge, station2bus = build_graph(routes)
        dis = [-1] * n
        q = deque()
        for bus in station2bus[source]:
            dis[bus] = 1
            q.append(bus)
        while q:
            x = q.popleft()
            for y in range(n):
                if edge[x][y] and dis[y] == -1:
                    dis[y] = dis[x] + 1
                    q.append(y)
        return min((dis[bus] for bus in station2bus[target] if dis[bus] != -1), default=-1)


def build_graph(routes):
    n = len(routes)
    edge = [[False] * n for _ in range(n)]
    station2bus = defaultdict(list)
    for i in range(n):
        for station in routes[i]:
            for j in station2bus[station]:
                edge[i][j] = edge[j][i] = True
            station2bus[station].append(i)
    return edge, station2bus
