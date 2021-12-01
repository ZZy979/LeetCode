class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []
        path = [[0, 0]]
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        visited = [[False] * c for i in range(r)]
        visited[0][0] = True
        return path if self.dfs(obstacleGrid, r, c, 0, 0, path, visited) else []
    
    def dfs(self, grid, r, c, x, y, path, visited):
        if x == r - 1 and y == c - 1:
            return True
        if y < c - 1 and grid[x][y + 1] == 0 and not visited[x][y + 1]:
            path.append([x, y + 1])
            visited[x][y + 1] = True
            if self.dfs(grid, r, c, x, y + 1, path, visited):
                return True
            path.pop()
        if x < r - 1 and grid[x + 1][y] == 0 and not visited[x + 1][y]:
            path.append([x + 1, y])
            visited[x + 1][y] = True
            if self.dfs(grid, r, c, x + 1, y, path, visited):
                return True
            path.pop()
        return False
