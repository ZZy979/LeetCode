from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        return max((x for x, n in cnt.items() if x == n), default=-1)
