from functools import cmp_to_key

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return ''.join(sorted((str(x) for x in nums), key=cmp_to_key(cmp)))

def cmp(a, b):
    return 1 if a + b > b + a else -1
