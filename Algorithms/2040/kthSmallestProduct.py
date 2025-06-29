import bisect

# 官方题解一：二分+二分，时间复杂度O(n1*log n2*log C)，空间复杂度O(1)，其中C=2*10^10+1
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        left, right = -10**10, 10**10
        while left <= right:
            mid = (left + right) // 2
            count = sum(f(nums2, x1, mid) for x1 in nums1)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

# nums中与x的乘积小于等于v的数目
def f(nums, x, v):
    if x > 0:
        return bisect.bisect_right(nums, v // x)
    elif x < 0:
        return len(nums) - bisect.bisect_left(nums, -(-v // x))
    else:
        return len(nums) if v >= 0 else 0
