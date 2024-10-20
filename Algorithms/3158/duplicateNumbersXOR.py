from functools import reduce
from operator import xor

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return reduce(xor, nums) ^ reduce(xor, set(nums))
