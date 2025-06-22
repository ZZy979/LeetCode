from math import comb

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        q = 10**9 + 7
        return comb(n - 1, k) * m * pow(m - 1, n - 1 - k, q) % q
