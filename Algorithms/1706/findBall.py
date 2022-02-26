class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(n):
            col = i
            for row in range(m):
                if grid[row][col] == 1:
                    if col == n - 1 or grid[row][col + 1] == -1:
                        ans.append(-1)
                        break
                    else:
                        col += 1
                else:
                    if col == 0 or grid[row][col - 1] == 1:
                        ans.append(-1)
                        break
                    else:
                        col -= 1
            else:
                ans.append(col)
        return ans
