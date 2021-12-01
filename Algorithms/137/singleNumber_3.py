# 官方题解3：数字电路设计，(ai, bi)=00, 01, 10分别表示当前遍历过的数字第i位之和除以3的余数是0, 1, 2（画真值表）
# 时间复杂度O(n)，空间复杂度O(1)
# 48 ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a, b = (~a & b & num) | (a & ~b & ~num), ~a & (b ^ num)
        return b
