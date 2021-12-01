# 矩阵乘法
# 时间复杂度O(kn³)，空间复杂度O(n²)
# 44 ms
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        adj = [[0] * n for _ in range(n)]
        for i, j in relation:
            adj[i][j] = 1
        res = adj
        for _ in range(k - 1):
            res = matmul(res, adj)
        return res[0][-1]


def matmul(a, b):
    m, n, p = len(a), len(a[0]), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
