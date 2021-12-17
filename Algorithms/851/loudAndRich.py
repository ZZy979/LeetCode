from collections import defaultdict

# 官方题解1：DFS
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        self.ans = [-1] * len(quiet)
        for i in range(len(quiet)):
            self.dfs(graph, quiet, i)
        return self.ans
    
    def dfs(self, graph, quiet, x):
        if self.ans[x] != -1:
            return
        self.ans[x] = x
        for y in graph[x]:
            self.dfs(graph, quiet, y)
            if quiet[self.ans[y]] < quiet[self.ans[x]]:
                self.ans[x] = self.ans[y]
