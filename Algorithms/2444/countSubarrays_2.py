# 官方题解：一次遍历，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        border = last_min = last_max = -1
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                border = i
                last_min = last_max = -1
            if x == minK:
                last_min = i
            if x == maxK:
                last_max = i
            if last_min != -1 and last_max != -1:
                res += min(last_min, last_max) - border
        return res
