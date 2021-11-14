class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == 0:
            return 0
        if a == -0x80000000 and b == -1:
            return 0x7fffffff
        negative = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        res = 0
        for i in range(31, -1, -1):
            if (a >> i) >= b:
                res += 1 << i
                a -= b << i
        return -res if negative else res
