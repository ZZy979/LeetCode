class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))
