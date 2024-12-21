import math
from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        m = n // math.gcd(*Counter(s).values())
        for k in range(m, n + 1, m):
            if n % k == 0 and all(sorted(s[i:i + k]) == sorted(s[:k]) for i in range(k, n, k)):
                break
        return k
