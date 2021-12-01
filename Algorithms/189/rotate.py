class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, n)
    
    def reverse(self, nums, lower, upper):
        left, right = lower, upper - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
