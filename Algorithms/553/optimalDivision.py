from functools import reduce
from operator import truediv

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        return backtrack(nums, len(nums))[1]


def backtrack(nums, end):
    if end == 1:
        return nums[0], str(nums[0])
    max_val, max_expr = 0, ''
    for i in range(1, end):
        numerator, expr = backtrack(nums, i)
        denominator = reduce(truediv, nums[i:end])
        if numerator / denominator > max_val:
            max_val = numerator / denominator
            max_expr = '{}/{}'.format(expr, nums[i]) if i == len(nums) - 1 \
                else '{}/({})'.format(expr, '/'.join(map(str, nums[i:end])))
    return max_val, max_expr
