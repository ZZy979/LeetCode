# 官方题解4：数字电路设计优化，先计算b后计算a
# 时间复杂度O(n)，空间复杂度O(1)
# 36 ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b
