# 官方题解二：双指针，时间复杂度O(n+q)，空间复杂度O(n)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        delta_array = [0] * (n + 1)
        operations = 0
        k = 0
        for i in range(n):
            num = nums[i]
            operations += delta_array[i]
            while k < len(queries) and operations < num:
                left, right, value = queries[k]
                delta_array[left] += value
                delta_array[right + 1] -= value
                if left <= i <= right:
                    operations += value
                k += 1
            if operations < num:
                return -1
        return k
