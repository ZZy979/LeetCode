# 方法2：剪枝
# 时间复杂度O(n²)，空间复杂度O(n)
# 44 ms
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        x_rows, x_cols = set(), set()
        o_rows, o_cols = set(), set()
        space = False
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'X':
                    x_rows.add(r)
                    x_cols.add(c)
                elif board[r][c] == 'O':
                    o_rows.add(r)
                    o_cols.add(c)
                elif board[r][c] == ' ':
                    space = True

        if any(row_all(board, r, 'X') for r in range(n) if r not in o_rows) \
            or any(column_all(board, c, 'X') for c in range(n) if c not in o_cols) \
            or main_diag_all(board, 'X') or sub_diag_all(board, 'X'):
            return 'X'
        elif any(row_all(board, r, 'O') for r in range(n) if r not in x_rows) \
            or any(column_all(board, c, 'O') for c in range(n) if c not in x_cols) \
            or main_diag_all(board, 'O') or sub_diag_all(board, 'O'):
            return 'O'
        elif space:
            return 'Pending'
        else:
            return 'Draw'


def row_all(board, row, char):
    return all(board[row][c] == char for c in range(len(board[row])))


def column_all(board, col, char):
    return all(board[r][col] == char for r in range(len(board)))


def main_diag_all(board, char):
    return all(board[i][i] == char for i in range(len(board)))


def sub_diag_all(board, char):
    n = len(board)
    return all(board[i][n - 1 - i] == char for i in range(n))
