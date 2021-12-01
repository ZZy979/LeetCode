# 方法1：散列表，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = set(nums)
        for x in nums:
            if target - x in nums:
                return [x, target - x]
        return []
