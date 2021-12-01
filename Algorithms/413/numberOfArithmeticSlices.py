class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        i, j = 0, 2
        ans = 0
        while i < n - 2:
            while j < n and nums[j] - nums[j - 1] == nums[j - 1] - nums[j - 2]:
                j += 1
            if (d := j - i) >= 3:
                ans += (d - 1) * (d - 2) // 2
            i = j - 1
            j += 1
        return ans
