class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 10:
            return 1
        # m * 10**k <= n < (m + 1) * 10**k
        k = len(str(n)) - 1
        m, r = divmod(n, 10**k)
        if m == 1:
            return self.countDigitOne(10**k - 1) + self.countDigitOne(r) + r + 1
        else:
            return m * self.countDigitOne(10**k - 1) + self.countDigitOne(r) + 10**k
