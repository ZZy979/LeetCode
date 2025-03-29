
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]
        # 对角线编号：k = i - j + n
        for k in range(1, m + n):
            min_j = max(n - k, 0)
            max_j = min(m + n - 1 - k, n - 1)
            s = set()
            for j in range(min_j, max_j + 1):
                i = k + j - n
                answer[i][j] = len(s)
                s.add(grid[i][j])
            s.clear()
            for j in range(max_j, min_j - 1, -1):
                i = k + j - n
                answer[i][j] = abs(answer[i][j] - len(s))
                s.add(grid[i][j])
        return answer
