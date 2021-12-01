import heapq

# 官方题解2：优先队列，时间复杂度O(klog n)，空间复杂度O(n)
# 2388 ms
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        q = [Frac(arr[0] / arr[i], 0, i) for i in range(1, len(arr))]
        heapq.heapify(q)
        for _ in range(k - 1):
            frac = heapq.heappop(q)
            i, j = frac.i, frac.j
            if i + 1 < j:
                heapq.heappush(q, Frac(arr[i + 1] / arr[j], i + 1, j))
        return [arr[q[0].i], arr[q[0].j]]


class Frac:

    def __init__(self, val, i, j):
        self.val = val
        self.i = i
        self.j = j

    def __lt__(self, other):
        return self.val < other.val
