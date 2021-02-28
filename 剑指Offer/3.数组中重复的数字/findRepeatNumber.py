# 方法1：哈希表
# 时间复杂度O(n)，空间复杂度O(n)
# 52 ms
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            else:
                seen.add(x)
