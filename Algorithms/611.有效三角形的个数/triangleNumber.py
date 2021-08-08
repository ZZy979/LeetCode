import bisect

# 排序+二分查找，时间复杂度O(n²log n)
# 2016 ms
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(x for x in nums if x > 0)
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect.bisect_left(nums, nums[i] + nums[j], lo=j + 1)
                ans += k - j - 1
        return ans
