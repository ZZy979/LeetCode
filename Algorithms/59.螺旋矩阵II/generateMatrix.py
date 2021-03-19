class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        r, c = 0, 0
        d = 0
        for i in range(1, n**2 + 1):
            matrix[r][c] = i
            nr, nc = r + directions[d][0], c + directions[d][1]
            if not (0 <= nr < n and 0 <= nc < n and matrix[nr][nc] is None):
                d = (d + 1) % 4
            r, c = r + directions[d][0], c + directions[d][1]
        return matrix
