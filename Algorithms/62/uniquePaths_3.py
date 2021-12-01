from math import comb

# 官方题解2：计算组合数（调库）
# 时间复杂度O(min{m, n})，空间复杂度O(1)
# 44 ms
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)
