from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for x in sorted(c, key=abs):
            if c[2 * x] < c[x]:
                return False
            c[2 * x] -= c[x]
            c[x] = 0
        return True
