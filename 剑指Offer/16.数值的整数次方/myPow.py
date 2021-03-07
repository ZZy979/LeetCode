class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return self.myPow(1 / x, -n)
        else:
            p = self.myPow(x, n // 2)
            return p * p if n % 2 == 0 else p * p * x
