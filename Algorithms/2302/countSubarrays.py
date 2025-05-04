import bisect
from itertools import accumulate

# 前缀和+二分查找，时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = list(accumulate(nums, initial=0))
        ans = 0
        for left in range(n):
            score = lambda r: (prefix_sum[r + 1] - prefix_sum[left]) * (r - left + 1)
            right = bisect.bisect_left(range(n), k, left, n, key=score)
            ans += right - left
        return ans
