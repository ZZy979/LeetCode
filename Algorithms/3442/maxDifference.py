from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        return max(n for n in cnt.values() if n % 2 == 1) - min(n for n in cnt.values() if n % 2 == 0)
