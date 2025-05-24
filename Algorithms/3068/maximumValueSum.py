# 官方题解一：贪心，时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = sum(nums)
        diff = [(x ^ k) - x for x in nums]
        diff.sort()
        i = len(diff) - 1
        while i > 0 and diff[i] + diff[i - 1] >= 0:
            res += diff[i] + diff[i - 1]
            i -= 2
        return res
