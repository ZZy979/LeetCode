# 方法2：双指针
# 时间复杂度O(n)，空间复杂度O(1)
# 56 ms
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left_max, right_max = height[0], height[-1]
        left, right = 1, n - 2
        ans = 0
        while left <= right:
            m = min(left_max, right_max)
            if m == left_max:
                if m > height[left]:
                    ans += m - height[left]
                left_max = max(left_max, height[left])
                left += 1
            else:
                if m > height[right]:
                    ans += m - height[right]
                right_max = max(right_max, height[right])
                right -= 1
        return ans
