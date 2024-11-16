class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = lambda s: min(s, 4 - s)
        ans = sum(
            f(grid[i][j] + grid[i][n - 1 - j] + grid[m - 1 - i][j] + grid[m - 1 - i][n - 1 - j])
            for i in range(m // 2) for j in range(n // 2)
        )
        # 中间行
        if m % 2 == 1:
            mid_row_flip = sum(grid[m // 2][j] != grid[m // 2][n - 1 - j] for j in range(n // 2))
            mid_row_no_flip_one = sum(grid[m // 2][j] == grid[m // 2][n - 1 - j] == 1 for j in range(n // 2))
            ans += mid_row_flip
        else:
            mid_row_flip = mid_row_no_flip_one = 0
        # 中间列
        if n % 2 == 1:
            mid_col_flip = sum(grid[i][n // 2] != grid[m - 1 - i][n // 2] for i in range(m // 2))
            mid_col_no_flip_one = sum(grid[i][n // 2] == grid[m - 1 - i][n // 2] == 1 for i in range(m // 2))
            ans += mid_col_flip
        else:
            mid_col_flip = mid_col_no_flip_one = 0
        if not mid_row_flip and not mid_col_flip and (mid_row_no_flip_one + mid_col_no_flip_one) % 2 == 1:
            ans += 2
        # 中心点
        if m % 2 == 1 and n % 2 == 1 and grid[m // 2][n // 2] == 1:
            ans += 1
        return ans
