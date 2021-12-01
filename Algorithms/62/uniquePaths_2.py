# 官方题解1：动态规划
# f(i, j)表示从左上角走到(i, j)的路径数量
# f(i, j) = f(i - 1, j) + f(i, j - 1), f(i, 0) = f(0, j) = 1
# 时间复杂度O(mn)，空间复杂度O(mn)
# 44 ms
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
