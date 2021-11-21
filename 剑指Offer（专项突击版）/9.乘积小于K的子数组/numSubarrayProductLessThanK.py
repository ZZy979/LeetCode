class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, prod, ans = 0, 1, 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
