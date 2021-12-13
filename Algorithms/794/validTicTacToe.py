class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        nx, no = count(board, 'X'), count(board, 'O')
        wx, wo = win(board, 'X'), win(board, 'O')
        return (wx and not wo and nx == no + 1) or (not wx and wo and nx == no) or (not wx and not wo and (nx == no or nx == no + 1))


def count(board, c):
    return sum(1 for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == c)


def win(board, c):
    n = len(board)
    s = c * n
    return any(row == s for row in board) \
        or any(col == s for col in map(''.join, zip(*board))) \
        or all(board[i][i] == c for i in range(n)) \
        or all(board[i][n - 1 - i] == c for i in range(n))
