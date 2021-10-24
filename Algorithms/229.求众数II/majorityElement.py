from collections import Counter

# 方法1：计数，时间复杂度O(n)，空间复杂度O(n)
# 32 ms
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v > len(nums) // 3]
