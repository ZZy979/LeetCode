import bisect

# 官方题解：排序+二分查找
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        rec = sorted(nums1)
        abs_sum = maxn = 0
        n = len(nums1)
        q = 10**9 + 7
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            abs_sum = (abs_sum + d) % q
            j = bisect.bisect_left(rec, nums2[i])
            if j < n:
                maxn = max(maxn, d - (rec[j] - nums2[i]))
            if j > 0:
                maxn = max(maxn, d - (nums2[i] - rec[j - 1]))
        return (abs_sum - maxn + q) % q
