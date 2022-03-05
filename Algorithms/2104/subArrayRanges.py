# 暴力法，时间复杂度O(n²)，空间复杂度O(1)
# 3804 ms
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            min_val = max_val = nums[i]
            for j in range(i + 1, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                ans += max_val - min_val
        return ans
