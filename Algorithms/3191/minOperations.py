class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                ans += 1
                for j in range(i, i + 3):
                    nums[j] = 1 - nums[j]
        return ans if nums[-2] == 1 and nums[-1] == 1 else -1
