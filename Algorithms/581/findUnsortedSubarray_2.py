class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        maximum, minimum = -0x80000000, 0x7fffffff
        for i in range(n):
            if maximum > nums[i]:
                right = i
            maximum = max(maximum, nums[i])
        for i in range(n - 1, -1, -1):
            if minimum < nums[i]:
                left = i
            minimum = min(minimum, nums[i])
        return 0 if left == right else right - left + 1
