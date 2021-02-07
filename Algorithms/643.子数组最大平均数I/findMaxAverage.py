class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = s = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            m = max(m, s)
        return m / k
