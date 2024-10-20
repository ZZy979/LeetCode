class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        p = [[0] * n for _ in range(m)]
        p[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    p[i][j] = 0
                else:
                    if i < m - 1:
                        p[i][j] += p[i + 1][j]
                    if j < n - 1:
                        p[i][j] += p[i][j + 1]
        return p[0][0]
