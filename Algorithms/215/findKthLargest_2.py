import heapq

# 官方题解2：大根堆
# 时间复杂度O(nlog n)，空间复杂度O(log n)
# 44 ms
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]
