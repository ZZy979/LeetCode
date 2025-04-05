from functools import reduce
from operator import xor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(reduce(xor, s, 0) for s in subsets(nums, 0))

def subsets(nums, start):
    if start == len(nums):
        yield []
    else:
        for s in subsets(nums, start + 1):
            yield s
            yield [nums[start]] + s
