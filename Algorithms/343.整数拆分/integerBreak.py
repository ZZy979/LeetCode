# 首先，不管把n拆成几个数，根据均值不等式，只有这几个数最接近时积才最大
# 假设将n拆成m个整数(2<=m<=n)，且n=km+r（k为整数，0<=r<m）
# 则将n拆成m-r个k和r个k+1时，这m个整数是最接近的，积为k^(m-r)*(k+1)^r
# 因此只要对m=2~n求这式子的最大值即可
class Solution:
    def integerBreak(self, n: int) -> int:
        p = 0
        for m in range(2, n + 1):
            k, r = divmod(n, m)
            p = max(p, k ** (m - r) * (k + 1) ** r)
        return p
