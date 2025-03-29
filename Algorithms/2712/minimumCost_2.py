from itertools import pairwise

# 官方题解：一次遍历
class Solution:
    def minimumCost(self, s: str) -> int:
        return sum(min(i, len(s) - i) for i, (x, y) in enumerate(pairwise(s), 1) if x != y)
