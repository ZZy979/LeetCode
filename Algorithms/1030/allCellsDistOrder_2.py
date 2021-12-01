# 官方题解：几何法（层序遍历），时间复杂度O(RC)
# 204 ms
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret
