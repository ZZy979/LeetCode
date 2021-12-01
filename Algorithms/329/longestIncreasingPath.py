class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        # a[i][j]: 从matrix[i][j]出发的最长递增路径长度
        self.a = [[0] * self.n for i in range(self.m)]
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(matrix, i, j))
        return ans
    
    def dfs(self, matrix, i, j):
        if self.a[i][j] != 0:
            return self.a[i][j]
        self.a[i][j] = 1
        for d in self.dirs:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < self.m and 0 <= nj < self.n and matrix[ni][nj] > matrix[i][j]:
                self.a[i][j] = max(self.a[i][j], self.dfs(matrix, ni, nj) + 1)
        return self.a[i][j]
