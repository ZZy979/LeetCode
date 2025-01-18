# 方法一：暴力法
# 时间复杂度O(n²)，空间复杂度O(1)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0xFFFFFFFF
        for i in range(n):
            value = 0
            for j in range(i, n):
                value |= nums[j]
                if value >= k:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != 0xFFFFFFFF else -1
