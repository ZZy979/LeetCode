# 评论区解法，时间复杂度O(n)
# 52 ms
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= n:
                n = 1
            else:
                n += 1
        return n == 1
