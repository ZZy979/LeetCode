from itertools import accumulate

# 官方题解：前缀和
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        p = list(accumulate(map(int, s), initial=0))
        return min(p[i] + (len(s) - i) - (p[-1] - p[i]) for i in range(len(p)))
