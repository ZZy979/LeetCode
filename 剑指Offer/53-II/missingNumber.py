class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[-1] == n - 1:
            return n
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return left
