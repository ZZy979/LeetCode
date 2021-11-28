class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
            ans = max(ans, largestRectangleArea(heights))
        return ans


def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(h * w, ans)
        stack.append(i)
    return ans
