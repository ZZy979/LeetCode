import heapq

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(k)]
