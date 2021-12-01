class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        y *= sign
        return y if -2**31 <= y < 2**31 else 0
