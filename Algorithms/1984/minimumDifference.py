class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i] - nums[i - k + 1] for i in range(k - 1, len(nums)))
