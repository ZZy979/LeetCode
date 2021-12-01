# 官方题解：数学
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s = start >> 1
        e = n & start & 1
        return (sum_xor(s - 1) ^ sum_xor(s + n - 1)) << 1 | e


def sum_xor(x):
    r = x % 4
    if r == 0:
        return x
    elif r == 1:
        return 1
    elif r == 2:
        return x + 1
    else:
        return 0
