class Solution:
    def countDigitOne(self, n: int) -> int:
        count, i = 0, 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return count
