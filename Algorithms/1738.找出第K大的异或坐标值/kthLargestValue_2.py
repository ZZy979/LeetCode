class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m) :
            for j in range(1, n) :
                matrix[i][j] ^= matrix[i][j - 1]
        for i in range(1, m) :
            for j in range(n) :
                matrix[i][j] ^= matrix[i - 1][j]
        line = sorted([c for r in matrix for c in r], reverse=True)
        return line[k - 1]
