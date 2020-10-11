class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in rows:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0
