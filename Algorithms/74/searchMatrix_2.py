# 一次二分查找，时间复杂度O(log mn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            m = matrix[mid // n][mid % n]
            if m == target:
                return True
            elif m < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
