# 方法3：二进制数
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [int2subset(nums, x) for x in range(2 ** len(nums))]


def int2subset(nums, x):
    subset = []
    i = 0
    while x:
        if x & 1:
            subset.append(nums[i])
        i += 1
        x >>= 1
    return subset
