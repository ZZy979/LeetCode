class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = list()
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            for r in range(top + 1, bottom + 1):
                ans.append(matrix[r][right])
            if left < right and top < bottom:
                for c in range(right - 1, left, -1):
                    ans.append(matrix[bottom][c])
                for r in range(bottom, top, -1):
                    ans.append(matrix[r][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ans
