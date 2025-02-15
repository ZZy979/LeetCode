# 官方题解：二分查找（最大值最小、最小值最大：考虑二分查找）
# 时间复杂度：O(nlog C)，空间复杂度O(1)，其中n是nums的长度，C是nums中的最大值
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right, ans = 1, max(nums), 0
        while left <= right:
            y = (left + right) // 2
            ops = sum((x - 1) // y for x in nums)
            if ops <= maxOperations:
                ans = y
                right = y - 1
            else:
                left = y + 1
        return ans
