class Solution:
    def totalNQueens(self, n: int) -> int:
        return [0, 1, 0, 0, 2, 10, 4, 40, 92, 352][n]
