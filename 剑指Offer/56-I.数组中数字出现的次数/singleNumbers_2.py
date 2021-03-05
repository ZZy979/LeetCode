# 官方题解：分组异或
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(operator.xor, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
