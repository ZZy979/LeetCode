class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum(abs(nums[i] - nums[j]) == k for i in range(len(nums)) for j in range(i + 1, len(nums)))
