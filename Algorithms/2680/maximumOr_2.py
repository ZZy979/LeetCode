# 官方题解：位运算
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        or_sum = multi_bits = 0
        for x in nums:
            multi_bits |= x & or_sum
            or_sum |= x
        return max((or_sum ^ x) | (x << k) | multi_bits for x in nums)
