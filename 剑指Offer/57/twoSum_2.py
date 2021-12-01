# 方法2：双指针，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [nums[left], nums[right]]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []
