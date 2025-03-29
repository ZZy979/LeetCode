class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                top_left = set(grid[r - k][c - k] for k in range(1, min(r, c) + 1))
                bottom_right = set(grid[r + k][c + k] for k in range(1, min(m - r, n - c)))
                answer[r][c] = abs(len(top_left) - len(bottom_right))
        return answer
