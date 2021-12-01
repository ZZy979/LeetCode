# 官方题解2：单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        return ans
