# 官方题解1：递归法枚举子集，时间复杂度O(2^n)，空间复杂度O(n)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(xor, idx):
            nonlocal res
            if idx == len(nums):
                res += xor
                return
            dfs(xor ^ nums[idx], idx + 1)
            dfs(xor, idx + 1)

        dfs(0, 0)
        return res
