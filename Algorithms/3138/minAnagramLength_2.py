from collections import Counter

# 官方题解
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for m in range(1, n):
            if n % m == 0 and all(Counter(s[:m]) == Counter(s[i:i + m]) for i in range(m, n, m)):
                return m
        return n
