from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c = Counter(''.join(sorted(set(word))) for word in words)
        return sum(n * (n - 1) // 2 for n in c.values())
