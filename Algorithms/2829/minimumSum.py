class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # 除[k//2+1, k-1]之外的前n个正整数即为和最小的k-avoiding数组
        if k // 2 >= n:
            return n * (n + 1) // 2
        m = k // 2
        return m * (m + 1) // 2 + (2 * k + n - m - 1) * (n - m) // 2
