import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        k = min(k, m * n)
        ans = []
        q = [(nums1[i] + nums2[0], i, 0) for i in range(m)]
        heapq.heapify(q)
        for _ in range(k):
            s, i, j = heapq.heappop(q)
            ans.append([nums1[i], nums2[j]])
            if j < n - 1:
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
