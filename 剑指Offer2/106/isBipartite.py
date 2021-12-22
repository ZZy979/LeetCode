class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.color = [0] * n  # 0 - uncolored, 1 - red, 2 - green
        self.valid = True
        for i in range(n):
            if self.color[i] == 0:
                self.dfs(graph, i, 1)
                if not self.valid:
                    return False
        return True
    
    def dfs(self, graph, node, color):
        self.color[node] = color
        neighbor_color = 3 - color
        for neighbor in graph[node]:
            if self.color[neighbor] == 0:
                self.dfs(graph, neighbor, neighbor_color)
                if not self.valid:
                    return
            elif self.color[neighbor] != neighbor_color:
                self.valid = False
                return
