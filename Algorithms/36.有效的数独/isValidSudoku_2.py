# 官方题解：一次遍历
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = ord(board[i][j]) - ord('1')
                    if row[i][x] or col[j][x] or block[i // 3][j // 3][x]:
                        return False
                    row[i][x] = col[j][x] = block[i // 3][j // 3][x] = True
        return True
