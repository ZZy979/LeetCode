from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        neighbors = defaultdict(list)
        for u, v in adjacentPairs:
            neighbors[u].append(v)
            neighbors[v].append(u)
        u = next(i for i in neighbors if len(neighbors[i]) == 1)
        ans = [u]
        for _ in range(n):
            v = neighbors[u][0]
            ans.append(v)
            neighbors[u].remove(v)
            neighbors[v].remove(u)
            u = v
        return ans
