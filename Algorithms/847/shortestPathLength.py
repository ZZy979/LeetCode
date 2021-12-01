from collections import deque

# 状态压缩+BFS
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(i, 1 << i, 0) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}
        while q:
            i, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                return dist
            for j in graph[i]:
                new_mask = mask | (1 << j)
                if (j, new_mask) not in visited:
                    q.append((j, new_mask, dist + 1))
                    visited.add((j, new_mask))
        return 0
