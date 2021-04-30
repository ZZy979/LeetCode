import math

# 官方题解1：使用sqrt函数
# 时间复杂度O(sqrt(c))
# 532 ms
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a**2 <= c:
            b = math.sqrt(c - a**2)
            if b == int(b):
                return True
            a += 1
        return False
