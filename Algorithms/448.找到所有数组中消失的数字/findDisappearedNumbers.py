# 移动元素
# 时间复杂度O(n)，空间复杂度O(1)
# 420 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            tmp, j = nums[i], nums[i] - 1
            while nums[j] != j + 1:
                tmp, nums[j], j = nums[j], tmp, nums[j] - 1
        print(nums)
        return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]
