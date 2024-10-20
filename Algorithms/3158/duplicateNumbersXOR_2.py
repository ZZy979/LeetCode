# 位运算
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = res = 0
        for x in nums:
            if seen & (1 << x):
                res ^= x
            else:
                seen |= (1 << x)
        return res
