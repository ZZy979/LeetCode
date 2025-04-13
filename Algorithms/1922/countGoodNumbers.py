class Solution:
    def countGoodNumbers(self, n: int) -> int:
        q = 10**9 + 7
        return pow(4, n // 2, q) * pow(5, (n + 1) // 2, q) % q
