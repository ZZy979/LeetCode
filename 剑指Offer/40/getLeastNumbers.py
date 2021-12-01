import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k == 0:
            return []
        heap = []
        for i in range(k):
            heapq.heappush(heap, -arr[i])
        for i in range(k, len(arr)):
            if arr[i] < -heap[0]:
                heapq.heapreplace(heap, -arr[i])
        return [-x for x in heap]
