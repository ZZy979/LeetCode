# 官方题解3：费马平方和定理
# 时间复杂度O(sqrt(c))
# 60 ms
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for base in range(2, int(sqrt(c)) + 1):
            if c % base != 0:
                continue
            exp = 0
            while c % base == 0:
                exp += 1
                c //= base
            if base % 4 == 3 and exp % 2 != 0:
                return False
        return c % 4 != 3
