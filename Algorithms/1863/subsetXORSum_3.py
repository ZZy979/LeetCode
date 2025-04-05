# 官方题解2：迭代法枚举子集，时间复杂度O(n*2^n)，空间复杂度O(1)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(1 << n):
            xor = 0
            for j in range(n):
                if i & (1 << j):
                    xor ^= nums[j]
            res += xor
        return res
