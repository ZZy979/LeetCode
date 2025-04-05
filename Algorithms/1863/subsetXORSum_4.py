from functools import reduce
from operator import or_

# https://leetcode.cn/problems/sum-of-all-subset-xor-totals/solutions/3614974/on-shu-xue-zuo-fa-pythonjavaccgojsrust-b-9txy/
# 按位考虑，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums) << (len(nums) - 1)
