# 官方题解2：判断质数优化
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(((1 << x.bit_count()) & 665772) != 0 for x in range(left, right + 1))
