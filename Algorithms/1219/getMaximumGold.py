class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(x: int, y: int, gold: int) -> None:
            gold += grid[x][y]
            nonlocal ans
            ans = max(ans, gold)

            rec = grid[x][y]
            grid[x][y] = 0

            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    dfs(nx, ny, gold)

            grid[x][y] = rec

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)

        return ans
