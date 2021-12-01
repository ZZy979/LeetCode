from collections import deque

# BFS
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        edges = {}
        for i, j in graph:
            if i != j:
                edges.setdefault(i, set()).add(j)
        queue = deque()
        queue.append(start)
        visited = {start}
        while queue:
            u = queue.popleft()
            if u == target:
                return True
            elif u in edges:
                for v in edges[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
        return False
