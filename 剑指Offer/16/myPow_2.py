class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x, n = 1 / x, -n
        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
