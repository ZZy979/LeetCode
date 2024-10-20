class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        return min((nums[i] + nums[n - 1 - i]) / 2 for i in range(n // 2))
