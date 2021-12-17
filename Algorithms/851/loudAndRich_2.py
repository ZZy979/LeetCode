from collections import defaultdict, deque

# 官方题解2：拓扑排序
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        ans = list(range(len(quiet)))
        q = deque(i for i, d in enumerate(indegree) if d == 0)
        while q:
            x = q.popleft()
            for y in graph[x]:
                if quiet[ans[x]] < quiet[ans[y]]:
                    ans[y] = ans[x]
                indegree[y] -= 1
                if indegree[y] == 0:
                    q.append(y)
        return ans
