import math

# 官方题解2：双指针
# 时间复杂度O(sqrt(c))
# 348 ms
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            s = a**2 + b**2
            if s == c:
                return True
            elif s < c:
                a += 1
            else:
                b -= 1
        return False
