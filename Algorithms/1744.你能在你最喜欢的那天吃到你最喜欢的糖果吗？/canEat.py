from itertools import accumulate

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        cumsum = list(accumulate(candiesCount, initial=0))
        return [c * (d + 1) > cumsum[t] and d < cumsum[t + 1] for t, d, c in queries]
