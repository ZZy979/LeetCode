# 方法1：对每一行进行二分查找，时间复杂度O(Mlog N)
# 52 ms
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            if matrix[r][0] > target:
                return False
            elif matrix[r][n - 1] < target:
                continue
            elif binsearch(matrix[r], target, 0, n - 1):
                return True
        return False


def binsearch(a, x, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if x == a[mid]:
        return True
    elif x < a[mid]:
        return binsearch(a, x, left, mid - 1)
    else:
        return binsearch(a, x, mid + 1, right)
