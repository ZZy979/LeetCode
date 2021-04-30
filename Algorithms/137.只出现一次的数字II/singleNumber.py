from collections import Counter

# 哈希表，时间复杂度O(n)，空间复杂度O(n)
# 40 ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for x in nums:
            if c[x] == 1:
                return x
