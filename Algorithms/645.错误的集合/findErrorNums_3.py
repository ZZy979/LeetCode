from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = Counter(nums)
        return [
            next(x for x in range(1, n + 1) if c[x] == 2),
            next(x for x in range(1, n + 1) if c[x] == 0)
        ]
