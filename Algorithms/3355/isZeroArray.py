from itertools import accumulate

# 官方题解：差分数组+前缀和，时间复杂度O(n+q)，空间复杂度O(n)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta_array = [0] * (len(nums) + 1)
        for left, right in queries:
            delta_array[left] += 1
            delta_array[right + 1] -= 1
        operations = list(accumulate(delta_array))
        return all(op >= x for op, x in zip(operations, nums))
