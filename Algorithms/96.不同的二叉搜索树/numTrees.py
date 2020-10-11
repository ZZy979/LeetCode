# 等价于求第n个卡特兰数
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        a = [0] * (n + 1)
        a[0] = a[1] = 1
        for i in range(2, n + 1):
            a[i] = sum(a[r] * a[i - r - 1] for r in range(n))
        return a[n]
