# 官方题解1：二分查找
# 时间复杂度O(nlog n)，空间复杂度O(1)
# 404 ms
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            cnt = sum(1 for x in nums if x <= mid)
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
