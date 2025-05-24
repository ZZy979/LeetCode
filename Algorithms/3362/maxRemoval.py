import heapq

# 官方题解：贪心+优先队列，时间复杂度O(n+qlog q)，空间复杂度O(n+q)
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        delta_array = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += delta_array[i]
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                delta_array[-heapq.heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)
