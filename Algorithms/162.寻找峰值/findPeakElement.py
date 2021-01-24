class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == n - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == n - 1 or nums[mid] < nums[mid + 1]):
                left = mid + 1
            else:
                right = mid - 1
