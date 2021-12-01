import math

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), math.ceil(len(A[0]) / 2)
        for i in range(m):
            for j in range(n):
                if A[i][j] == A[i][-j - 1]:
                    A[i][j] = A[i][-j - 1] = 1 - A[i][j]
        return A
