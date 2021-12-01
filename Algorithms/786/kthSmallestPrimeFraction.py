import heapq

# 暴力法，时间复杂度O(n²log n)，空间复杂度O(n²)
# 1656 ms
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, ((arr[i], arr[j]) for i in range(len(arr)) for j in range(i + 1, len(arr))), key=lambda x: x[0] / x[1])[-1]
