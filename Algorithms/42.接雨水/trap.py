# 方法1：针对暴力解法用空间换时间
# 时间复杂度O(n)，空间复杂度O(n)
# 48 ms
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(1, n - 1):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in range(n - 2, 0, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        ans = 0
        for i in range(1, n - 1):
            m = min(left_max[i], right_max[i])
            if height[i] < m:
                ans += m - height[i]
        return ans
