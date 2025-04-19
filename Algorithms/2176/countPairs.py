class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return sum(i * j % k == 0 and nums[i] == nums[j] for i in range(n - 1) for j in range(i + 1, n))
