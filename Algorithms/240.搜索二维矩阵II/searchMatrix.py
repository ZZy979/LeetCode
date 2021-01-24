# 线性搜索，时间复杂度O(m+n)
# 188 ms
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        while 0 <= r < m and 0 <= c < n:
            if target < matrix[r][c]:
                r -= 1
            elif target > matrix[r][c]:
                c += 1
            elif target == matrix[r][c]:
                return True
        return False
