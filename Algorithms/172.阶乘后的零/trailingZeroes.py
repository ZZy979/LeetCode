# 官方题解（方法3）
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros
