# 方法2：直接排序，两两交换元素
# 时间复杂度O(nlog n)，空间复杂度O(1)
# 36 ms
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
