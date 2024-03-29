from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max((c[k] + c[k + 1] for k in sorted(c) if k + 1 in c), default=0)
