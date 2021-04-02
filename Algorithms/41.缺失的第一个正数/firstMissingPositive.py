# 官方题解1：用nums[x]<0表示x+1出现
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for x in nums:
            x = abs(x)
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
