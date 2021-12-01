class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = [matrix[0][0]]
        matrix[0][0] = None
        r, c = 0, 0
        while True:
            walked = False
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                while True:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] is not None):
                        break
                    r, c = nr, nc
                    ans.append(matrix[r][c])
                    matrix[r][c] = None
                    walked = True
            if not walked:
                break
        return ans
