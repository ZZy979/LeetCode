# 循环计算可达性，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = calc_distance(edges, node1)
        dist2 = calc_distance(edges, node2)
        min_dist, node = 99999, -1
        for i in range(n):
            if (d := max(dist1[i], dist2[i])) < min_dist:
                min_dist, node = d, i
        return node

def calc_distance(edges, node):
    n = len(edges)
    dist = [99999] * n
    dist[node] = d = 0
    visited = {node}
    while (node := edges[node]) != -1:
        if node in visited:
            break
        visited.add(node)
        d += 1
        dist[node] = d
    return dist
