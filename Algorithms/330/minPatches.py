# 官方题解：贪心算法
# 时间复杂度O(m+log n)，空间复杂度O(1)
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0
        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1
        return patches
