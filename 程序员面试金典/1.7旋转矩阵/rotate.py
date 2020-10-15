class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2):
            layer_len = n - 2 * layer
            for i in range(layer_len - 1):
                x, y = layer, layer + i
                temp = matrix[x][y]
                for k in range(4):
                    x2, y2 = y, n - 1 - x
                    matrix[x2][y2], temp = temp, matrix[x2][y2]
                    x, y = x2, y2
