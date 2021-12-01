from functools import reduce
from itertools import chain
from operator import xor

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = reduce(xor, nums) ^ reduce(xor, range(1, n + 1))
        lowbit = x & (-x)
        x0 = x1 = 0
        for i in chain(nums, range(1, n + 1)):
            if i & lowbit == 0:
                x0 ^= i
            else:
                x1 ^= i
        return [x0, x1] if x0 in nums else [x1, x0]
