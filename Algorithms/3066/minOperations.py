import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, 2 * x + y)
            ans += 1
        return ans
