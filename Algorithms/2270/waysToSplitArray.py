from itertools import accumulate, islice

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n, s = len(nums), sum(nums)
        return sum(p >= s / 2 for p in islice(accumulate(nums), n - 1))
