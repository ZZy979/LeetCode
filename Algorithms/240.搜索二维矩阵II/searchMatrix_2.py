# 官方题解：搜索空间的缩减，时间复杂度O(nlog n)
# 228 ms
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        return search(matrix, target, 0, 0, len(matrix[0]) - 1, len(matrix) - 1)


def search(matrix, target, left, up, right, down):
    if left > right or up > down:
        return False
    # `target` is already larger than the largest element or smaller
    # than the smallest element in this submatrix.
    elif target < matrix[up][left] or target > matrix[down][right]:
        return False

    mid = left + (right-left)//2
    # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
    row = up
    while row <= down and matrix[row][mid] <= target:
        if matrix[row][mid] == target:
            return True
        row += 1
    return search(matrix, target, left, row, mid - 1, down) or search(matrix, target, mid + 1, up, right, row-1)
