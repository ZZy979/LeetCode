import math

# 官方题解：数学，时间复杂度O(sqrt(n))
# 60 ms
class Solution:
    def numSquares(self, n: int) -> int:
        if is_perfect_square(n):
            return 1
        elif check_answer4(n):
            return 4
        elif any(is_perfect_square(n - i**2) for i in range(1, math.isqrt(n) + 1)):
            return 2
        else:
            return 3


def is_perfect_square(x):
    return math.isqrt(x)**2 == x


def check_answer4(x):
    while x % 4 == 0:
        x //= 4
    return x % 8 == 7
