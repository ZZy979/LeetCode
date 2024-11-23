from collections import defaultdict, Counter

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        count = defaultdict(Counter)
        for x, y in pick:
            count[x][y] += 1
        return sum(any(n > p for n in c.values()) for p, c in count.items())
