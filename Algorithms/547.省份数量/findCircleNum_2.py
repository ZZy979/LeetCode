# 官方题解1：深度优先搜索，时间复杂度O(n²)，空间复杂度O(n)
# 48 ms
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
