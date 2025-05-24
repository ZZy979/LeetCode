# 官方题解三：状态机动态规划，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        f0, f1 = 0, float('-inf')
        for x in nums:
            t = max(f1 + x, f0 + (x ^ k))
            f0, f1 = max(f0 + x, f1 + (x ^ k)), t
        return f0
