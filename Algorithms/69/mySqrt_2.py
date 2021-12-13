class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        t = x
        while t > x / t:
            t = (t + x / t) // 2
        return int(t)
