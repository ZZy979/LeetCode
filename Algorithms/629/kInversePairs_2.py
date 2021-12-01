# 官方题解：动态规划，时间复杂度O(nk)，空间复杂度O(k)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        f = [1] + [0] * k
        r = 10**9 + 7
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(k + 1):
                g[j] = ((g[j - 1] if j >= 1 else 0) - (f[j - i] if j >= i else 0) + f[j]) % r
            f = g
        return f[k]
