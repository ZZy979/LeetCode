# 官方题解：等差数列
class Solution:
    def lastRemaining(self, n: int) -> int:
        k, a1, d = 0, 1, 1
        while n > 1:
            if k % 2 == 0 or n % 2 == 1:
                a1 += d
            k += 1
            n >>= 1
            d <<= 1
        return a1
