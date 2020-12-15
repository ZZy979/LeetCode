# 评论区解法
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        i = 1
        while i <= N // 10:
            n = N // i % 100
            i *= 10
            if n // 10 > n % 10:
                N = N // i * i - 1
        return N
