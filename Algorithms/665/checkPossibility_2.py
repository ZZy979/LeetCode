class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count += 1
                if 2 <= i < n - 1 and nums[i + 1] < nums[i - 1] and nums[i] < nums[i - 2]:
                    return False
                if count > 1:
                    return False
        return True
