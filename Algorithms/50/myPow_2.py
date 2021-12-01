class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return self.myPow(1 / x, -n)
        p = self.myPow(x, n // 2)
        p *= p
        if n % 2 == 1:
            p *= x
        return p
