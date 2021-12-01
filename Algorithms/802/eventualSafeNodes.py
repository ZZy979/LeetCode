from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = [[] for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                rev_graph[j].append(i)
        
        outdegree = [len(graph[i]) for i in range(n)]
        q = deque([i for i in range(n) if outdegree[i] == 0])
        ans = []
        while q:
            i = q.popleft()
            ans.append(i)
            for j in rev_graph[i]:
                outdegree[j] -= 1
                if outdegree[j] == 0:
                    q.append(j)
        return sorted(ans)
