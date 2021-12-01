class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        p = 1.0
        i = n
        while i:
            if i % 2 != 0:
                p *= x
            x *= x
            i //= 2
        return p
