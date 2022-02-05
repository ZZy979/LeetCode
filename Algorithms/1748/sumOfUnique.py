from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(x for x, n in Counter(nums).items() if n == 1)
