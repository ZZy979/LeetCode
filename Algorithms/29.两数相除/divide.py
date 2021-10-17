class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -0x80000000 and divisor == -1:
            return 0x7fffffff
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                res += 1 << i
                dividend -= divisor << i
        return -res if negative else res
