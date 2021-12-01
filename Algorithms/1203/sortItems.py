from collections import deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_graph, group_indegree = [[] for _ in range(n + m)], [0] * (n + m)
        item_graph, item_indegree = [[] for _ in range(n)], [0] * n

        group_item = [[] for _ in range(n + m)]
        p = m
        for i in range(n):
            if group[i] == -1:
                group[i] = p
                p += 1
            group_item[group[i]].append(i)
        
        for i in range(n):
            p = group[i]
            for j in beforeItems[i]:
                q = group[j]
                if q == p:
                    item_graph[j].append(i)
                    item_indegree[i] += 1
                else:
                    group_graph[q].append(p)
                    group_indegree[p] += 1
        
        group_topo_sort = topo_sort(group_graph, group_indegree, list(range(n + m)))
        if not group_topo_sort:
            return []
        ans = []
        for p in group_topo_sort:
            if not group_item[p]:
                continue
            item_topo_sort = topo_sort(item_graph, item_indegree, group_item[p])
            if not item_topo_sort:
                return []
            ans.extend(item_topo_sort)
        return ans


def topo_sort(graph, indegree, items):
    q = deque([i for i in items if indegree[i] == 0])
    res = []
    while q:
        i = q.popleft()
        res.append(i)
        for j in graph[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    return res if len(res) == len(items) else []
