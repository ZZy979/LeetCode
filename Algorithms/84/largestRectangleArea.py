# 官方题解：单调栈
# 时间复杂度O(n)，空间复杂度O(n)
# 260 ms
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left, right = [0] * n, [n] * n
        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))
