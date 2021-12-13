class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] == nums[mid + 1] and mid % 2 == 0 or nums[mid] == nums[mid - 1] and mid % 2 == 1:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
