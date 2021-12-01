import functools
import operator

# 计算组合数：P(m, n) = C(m + n - 2, n - 1) = (m + n - 2)! / ((m - 1)!(n - 1)!)
# 时间复杂度O(min{m, n})，空间复杂度O(1)
# 32 ms
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        if n == 1:
            return 1
        ans = functools.reduce(operator.mul, range(m, m + n - 1))
        return functools.reduce(operator.floordiv, range(1, n), ans)
