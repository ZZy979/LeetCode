class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        return max(abs(nums[i] - nums[(i + 1) % n]) for i in range(n))
