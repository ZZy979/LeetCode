class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0)
    
    def solve(self, board, index):
        if index == 81:
            return True
        x, y = divmod(index, 9)
        if board[x][y] != '.':
            return self.solve(board, index + 1)
        else:
            for n in range(1, 10):
                if self.check(board, x, y, str(n)):
                    board[x][y] = str(n)
                    if self.solve(board, index + 1):
                        return True
            board[x][y] = '.'
            return False
    
    def check(self, board, x, y, n):
        if n in board[x]:
            return False
        for i in range(9):
            if board[i][y] == n:
                return False
        r, c = x // 3, y // 3
        for i in range(3):
            for j in range(3):
                if board[r * 3 + i][c * 3 + j] == n:
                    return False
        return True
