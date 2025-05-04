# 官方题解：滑动窗口，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = total = left = 0
        for right in range(n):
            total += nums[right]
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            res += right - left + 1
        return res
