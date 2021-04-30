class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = functools.reduce(operator.xor, nums)
        d = 1
        while x & d == 0:
            d <<= 1
        a = b = 0
        for n in nums:
            if n & d:
                a ^= n
            else:
                b ^= n
        return [a, b]
