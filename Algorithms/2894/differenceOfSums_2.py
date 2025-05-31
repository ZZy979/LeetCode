class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        return n * (n + 1) // 2 - k * (k + 1) * m
