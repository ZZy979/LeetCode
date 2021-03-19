class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        total = m * n
        ans = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = 0, 0
        d = 0
        for i in range(total):
            ans[i] = matrix[r][c]
            visited[r][c] = True
            nr, nc = r + directions[d][0], c + directions[d][1]
            if not (0 <= nr < m and 0 <= nc < n and not visited[nr][nc]):
                d = (d + 1) % 4
            r += directions[d][0]
            c += directions[d][1]
        return ans
