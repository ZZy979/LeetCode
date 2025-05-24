# 官方题解一：差分数组+二分查找，时间复杂度O((n+q)log n)，空间复杂度O(n)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)
        if not check(nums, queries, right):
            return -1
        while left < right:
            k = (left + right) // 2
            if check(nums, queries, k):
                right = k
            else:
                left = k + 1
        return left

def check(nums, queries, k):
    delta_array = [0] * (len(nums) + 1)
    for left, right, value in queries[:k]:
        delta_array[left] += value
        delta_array[right + 1] -= value
    operations = list(accumulate(delta_array))
    return all(op >= x for op, x in zip(operations, nums))
