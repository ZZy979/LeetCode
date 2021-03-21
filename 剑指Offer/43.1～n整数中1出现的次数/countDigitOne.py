import math

class Solution:
    def __init__(self):
        self.memo = {}

    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 10:
            return 1
        if n in self.memo:
            return self.memo[n]
        # m * 10**k <= n < (m + 1) * 10**k
        k = int(math.log10(n))
        m = n // 10**k
        lower = m * 10**k
        if m == 1:
            ans = self.countDigitOne(lower - 1) + self.countDigitOne(n - lower) + n - (lower - 1)
        else:
            ans = self.countDigitOne(lower - 1) + self.countDigitOne(n - lower)
        self.memo[n] = ans
        return ans
