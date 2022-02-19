class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid] == nums[mid - 1]:
                mid -= 1
            if (mid - left) % 2 == 1:
                right = mid - 1
            else:
                left = mid + 2
        return nums[left]
