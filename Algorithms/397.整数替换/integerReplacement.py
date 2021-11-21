from functools import lru_cache

class Solution:
    def integerReplacement(self, n: int) -> int:
        return min_replace(n)


@lru_cache
def min_replace(n):
    return 0 if n == 1 else min_replace(n // 2) + 1 if n % 2 == 0 else min(min_replace(n + 1), min_replace(n - 1)) + 1
