import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx = heapq.nlargest(k, range(len(nums)), lambda i: nums[i])
        return [nums[i] for i in sorted(idx)]
