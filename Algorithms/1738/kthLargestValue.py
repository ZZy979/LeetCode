from heapq import nlargest
from itertools import chain

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                xor_matrix[i + 1][j + 1] = xor_matrix[i][j + 1] ^ xor_matrix[i + 1][j] ^ xor_matrix[i][j] ^ matrix[i][j]
        return nlargest(k, chain.from_iterable(xor_matrix))[-1]
