class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n
        for i in range(n):
            col = i
            for row in range(m):
                d = grid[row][col]
                col += d
                if not 0 <= col < n or grid[row][col] != d:
                    break
            else:
                ans[i] = col
        return ans
