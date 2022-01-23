class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # 设长度为n的序列以a, e, i, o, u结尾的个数分别为a[n], e[n], i[n], o[n], u[n]，则
        # ┌ a(n+1) ┐   ┌ 0 1 1 0 1 ┐┌ a(n) ┐
        # | e(n+1) |   | 1 0 1 0 0 || e(n) |
        # | i(n+1) | = | 0 1 0 1 0 || e(n) |
        # | o(n+1) |   | 0 0 1 0 0 || e(n) |
        # └ u(n+1) ┘   └ 0 0 1 1 0 ┘└ u(n) ┘
        # 即X(n+1)=AX(n) => X(n)=A^(n-1)X(1), X(1)=(1,1,1,1,1)^T
        # 使用矩阵快速幂
        if n == 1:
            return 5
        a = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]]
        p = matpow(a, n - 1)
        return sum(sum(r) for r in p) % (10**9 + 7)


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % (10**9 + 7) for j in range(len(b[0]))] for i in range(len(a))]


def matpow(a, n):
    if n == 1:
        return a
    p = matpow(a, n // 2)
    p = matmul(p, p)
    return p if n % 2 == 0 else matmul(p, a)
