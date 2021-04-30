import math

# 枚举b，二分查找a
# 时间复杂度O(sqrt(c)log(sqrt(c)))
# 6400 ms
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for b in range(int(math.sqrt(c)) + 1):
            left, right = 0, b
            while left <= right:
                a = (left + right) // 2
                s = a**2 + b**2
                if s == c:
                    return True
                elif s < c:
                    left = a + 1
                else:
                    right = a - 1
        return False
