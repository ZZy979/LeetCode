# 回溯法，超时。。
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = [[False] * cols for _ in range(rows)]
        return backtrack(heights, visited, 0, 0x7fffffff, 0, 0)


def backtrack(heights, visited, max_diff, min_effort, r, c):
    if r == len(heights) - 1 and c == len(heights[r]) - 1:
        return max_diff
    visited[r][c] = True
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(heights) and 0 <= nc < len(heights[nr]) and not visited[nr][nc] and abs(heights[r][c] - heights[nr][nc]) < min_effort:
            min_effort = min(min_effort, backtrack(heights, visited, max(max_diff, abs(heights[r][c] - heights[nr][nc])), min_effort, nr, nc))
    visited[r][c] = False
    return min_effort
