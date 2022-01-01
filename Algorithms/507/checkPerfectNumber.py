import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        r = math.isqrt(num)
        return num == (1 + sum(i + num // i for i in range(2, r + 1) if num % i == 0) - (r if r ** 2 == num else 0))
