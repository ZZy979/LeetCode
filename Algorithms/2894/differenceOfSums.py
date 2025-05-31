class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n + 1) // 2 - 2 * sum(range(m, n + 1, m))
