class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.dfs(graph, 0, [0])
        return self.ans

    def dfs(self, graph, i, path):
        if i == len(graph) - 1:
            self.ans.append(path.copy())
            return
        for j in graph[i]:
            path.append(j)
            self.dfs(graph, j, path)
            path.pop()
