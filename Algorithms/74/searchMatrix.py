import bisect

# 两次二分查找，时间复杂度O(log m+log n)=O(log mn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect.bisect_right([row[0] for row in matrix], target)
        if i == 0:
            return False
        i -= 1
        j = bisect.bisect_left(matrix[i], target)
        return j < len(matrix[i]) and matrix[i][j] == target
