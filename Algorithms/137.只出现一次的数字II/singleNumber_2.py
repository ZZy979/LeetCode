# 官方题解2：依次确定每一个二进制位，答案的第i个二进制位就是数组中所有元素的第i个二进制位之和除以3的余数
# 时间复杂度O(nlog C)，C是数据范围，空间复杂度O(1)
# 112 ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
