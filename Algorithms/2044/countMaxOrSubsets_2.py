from functools import reduce
from operator import or_

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = reduce(or_, nums)
        return dfs(nums, 0, 0, max_val)


def dfs(nums, start, or_val, max_val):
    if or_val == max_val:
        # 剪枝
        return 1 << (len(nums) - start)
    elif start >= len(nums):
        return 0
    return dfs(nums, start + 1, or_val | nums[start], max_val) + dfs(nums, start + 1, or_val, max_val)
