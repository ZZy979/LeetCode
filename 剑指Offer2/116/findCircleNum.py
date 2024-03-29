class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        circles = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(isConnected, visited, i)
                circles += 1
        return circles


def dfs(isConnected, visited, i):
    for j in range(len(isConnected)):
        if isConnected[i][j] == 1 and j not in visited:
            visited.add(j)
            dfs(isConnected, visited, j)
